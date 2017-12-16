from abc import abstractmethod
from enum import IntEnum

from ff6.bin_util import BinaryObject

def _value_in_range(name, val, min_val, max_val):
    val = int(val)
    return val >= min_val and val <= max_val

class InvalidFieldValueError(ValueError):

    def __init__(self, name, value):
        super().__init__('Invalid value for %s: %s' % (name, value))

class FieldType(IntEnum):
    Scalar = 1
    Struct = 2
    Array  = 3

class ByteSide(IntEnum):
    Low  = 1
    High = 2

class AbstractField:

    def __init__(self, name, offset, serializer=None, deserializer=None):
        self.name = name
        self.offset = offset
        self.serializer = serializer
        self.deserializer = deserializer

    def check_serialized_value(self, value):
        return True

    def check_deserialized_value(self, value):
        return True

    @abstractmethod
    def _serialize(self, bin_obj, location, value):
        raise NotImplementedError()

    @abstractmethod
    def _deserialize(self, bin_obj, location):
        raise NotImplementedError()

    def serialize(self, bin_obj, location, value):
        if not self.check_serialized_value(value):
            raise InvalidFieldValueError(self.name, value)
        if self.serializer:
            value = self.serializer(value)
        self._serialize(bin_obj, location, value)

    def deserialize(self, bin_obj, location):
        value = self._deserialize(bin_obj, location)
        if not self.check_deserialized_value(value):
            raise InvalidFieldValueError(self.name, value)
        if self.deserializer:
            return self.deserializer(value)
        return value

class AbstractScalarField(AbstractField):

    FieldType = FieldType.Scalar

class AbstractStructField(AbstractField):

    FieldType = FieldType.Struct

class AbstractArrayField(AbstractField):

    FieldType = FieldType.Array

class NumberRangeCheckMixin:

    MinValue = 0
    MaxValue = 0

    def check_serialized_value(self, value):
        return _value_in_range(self.name, value, self.MinValue, self.MaxValue)

    def check_deserialized_value(self, value):
        return _value_in_range(self.name, value, self.MinValue, self.MaxValue)

class EnumField(AbstractScalarField):

    def __init__(self, name, enum, offset, serializer=None, deserializer=None):
        super().__init__(name, offset, serializer, deserializer)
        self.enum = enum

    def check_serialized_value(self, value):
        for e in self.enum:
            if value == e.value:
                return True
        return False

    def check_deserialized_value(self, value):
        for e in self.enum:
            if value == e:
                return True
        return False

    @property
    def byte_length(self):
        max_val = list(self.enum)[-1]
        bit_length = max_val.bit_length()
        byte_length = bit_length // 8
        if bit_length % 8 > 0:
            byte_length += 1
        return byte_length

    def _serialize(self, bin_obj, location, value):
        bytes = value.to_bytes(self.byte_length, 'little')
        bin_obj.write_bytes(location + self.offset, bytes)

    def _deserialize(self, bin_obj, location):
        start = location + self.offset
        end = start + self.byte_length
        bytes = bin_obj.data[start:end]
        return self.enum.from_bytes(bytes, 'little')

class ShortEnumFieldMixin:

    ByteSide = ByteSide.Low
    BitSize  = 0

    def _serialize(self, bin_obj, location, value):
        value = value.value
        if self.ByteSide == ByteSide.High:
            func = bin_obj.write_high_bits
        else:
            func = bin_obj.write_low_bits
        func(location + self.offset, self.BitSize, value)

    def _deserialize(self, bin_obj, location):
        if self.ByteSide == ByteSide.High:
            func = bin_obj.read_high_bits
        else:
            func = bin_obj.read_low_bits
        return self.enum(func(location + self.offset, self.BitSize))

class Enum6LowField(ShortEnumFieldMixin, EnumField):

    ByteSide = ByteSide.Low
    BitSize  = 6

class Enum4HighField(ShortEnumFieldMixin, EnumField):

    ByteSide = ByteSide.High
    BitSize = 4

class Enum4LowField(ShortEnumFieldMixin, EnumField):

    ByteSide = ByteSide.Low
    BitSize = 4

class Enum3HighField(ShortEnumFieldMixin, EnumField):

    ByteSide = ByteSide.High
    BitSize  = 3

class Enum3LowField(ShortEnumFieldMixin, EnumField):

    ByteSide = ByteSide.Low
    BitSize  = 3

class FlagsField(EnumField):

    def check_serialized_value(self, value):
        for e in self.enum:
            if value & e.value:
                value &= ~e.value
        return value == 0

    def check_deserialized_value(self, value):
        for e in self.enum:
            if value & e:
                value &= ~e
        return value == 0

class Flags4HighField(ShortEnumFieldMixin, FlagsField):

    ByteSide = ByteSide.High
    BitSize  = 4

class U3HighField(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = 0
    MaxValue = 7

    def _serialize(self, bin_obj, location, value):
        bin_obj.write_high_bits(location + self.offset, 3, value)

    def _deserialize(self, bin_obj, location):
        return bin_obj.read_high_bits(location + self.offset, 3)

class U3LowField(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = 0
    MaxValue = 7

    def _serialize(self, bin_obj, location, value):
        bin_obj.write_low_bits(location + self.offset, 3, value)

    def _deserialize(self, bin_obj, location):
        return bin_obj.read_low_bits(location + self.offset, 3)

class S4HighField(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = -8
    MaxValue = 7

    def _serialize(self, bin_obj, location, value):
        bin_obj.write_high_bits(location + self.offset, 4, value)

    def _deserialize(self, bin_obj, location):
        return bin_obj.read_high_signed_bits(location + self.offset, 4)

class S4LowField(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = -8
    MaxValue = 7

    def _serialize(self, bin_obj, location, value):
        bin_obj.write_low_bits(location + self.offset, 4, value)

    def _deserialize(self, bin_obj, location):
        return bin_obj.read_low_signed_bits(location + self.offset, 4)

class U4HighField(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = 0
    MaxValue = 15

    def _serialize(self, bin_obj, location, value):
        bin_obj.write_high_bits(location + self.offset, 4, value)

    def _deserialize(self, bin_obj, location):
        return bin_obj.read_high_bits(location + self.offset, 4)

class U4LowField(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = 0
    MaxValue = 15

    def _serialize(self, bin_obj, location, value):
        bin_obj.write_low_bits(location + self.offset, 4, value)

    def _deserialize(self, bin_obj, location):
        return bin_obj.read_low_bits(location + self.offset, 4)

class U5HighField(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = 0
    MaxValue = 31

    def _serialize(self, bin_obj, location, value):
        bin_obj.write_low_bits(location + self.offset, 5, value)

    def _deserialize(self, bin_obj, location):
        return bin_obj.read_low_bits(location + self.offset, 5)

class U5LowField(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = 0
    MaxValue = 31

    def _serialize(self, bin_obj, location, value):
        bin_obj.write_low_bits(location + self.offset, 5, value)

    def _deserialize(self, bin_obj, location):
        return bin_obj.read_low_bits(location + self.offset, 5)

class U6LowField(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = 0
    MaxValue = 63

    def _serialize(self, bin_obj, location, value):
        bin_obj.write_low_bits(location + self.offset, 6, value)

    def _deserialize(self, bin_obj, location):
        return bin_obj.read_low_bits(location + self.offset, 6)

class U8Field(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = 0
    MaxValue = 255

    def _serialize(self, bin_obj, location, value):
        bin_obj.write_byte(location + self.offset, value)

    def _deserialize(self, bin_obj, location):
        value = bin_obj.read_byte(location + self.offset)
        return value

class U16Field(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = 0
    MaxValue = 65535

    def _serialize(self, bin_obj, location, value):
        bin_obj.write_short(location + self.offset, value)

    def _deserialize(self, bin_obj, location):
        return bin_obj.read_short(location + self.offset)

class U24Field(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = 0
    MaxValue = 16777215

    def _serialize(self, bin_obj, location, value):
        bin_obj.write_24(location + self.offset, value)

    def _deserialize(self, bin_obj, location):
        return bin_obj.read_24(location + self.offset)

class TimestampField(AbstractScalarField):

    def _serialize(self, bin_obj, location, timestamp):
        bin_obj.write_timestamp(location + self.offset, timestamp)

    def _deserialize(self, bin_obj, location):
        return bin_obj.read_timestamp(location + self.offset)

class U32Field(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = 0
    MaxValue = 4294967295

    def _serialize(self, bin_obj, location, value):
        bin_obj.write_int(location + self.offset, value)

    def _deserialize(self, bin_obj, location):
        return bin_obj.read_int(location + self.offset)

class ByteField(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = 0
    MaxValue = 255

    def _serialize(self, bin_obj, location, value):
        bin_obj.write_byte(location + self.offset, value)

    def _deserialize(self, bin_obj, location):
        return bin_obj.read_byte(location + self.offset)

class BattleStrField(AbstractScalarField):

    def __init__(self, name, size, offset, serializer=None, deserializer=None):
        super().__init__(name, offset, serializer, deserializer)
        self.size = size

    def _serialize(self, bin_obj, location, value):
        bin_obj.write_dte_battle_string(location + self.offset, self.size,
                                        value)

    def _deserialize(self, bin_obj, location):
        return bin_obj.read_dte_battle_string(location + self.offset,
                                              self.size)

class BitField(AbstractScalarField):

    __slots__ = (
        'obj',
        'name',
        'bit_index',
        'offset',
        'transform_incoming_binary_value',
        'transform_outgoing_binary_value',
    )

    def __init__(self, name, index, offset, serializer=None,
                 deserializer=None):
        super().__init__(name, offset, serializer, deserializer)
        self.index = index

    def check_serialized_value(self, value):
        return value == 0 or value == 1

    def check_deserialized_value(self, value):
        return isinstance(value, bool)

    @property
    def _binary_value(self):
        value = self.value
        if value is True:
            return 1 << self.bit_index
        if value is False:
            return 0

    @_binary_value.setter
    def _binary_value(self, new_value):
        if new_value == 1:
            self.value = True
        if new_value == 0:
            self.value = False

    def _serialize(self, bin_obj, location, value):
        bin_obj.write_bit(location + self.offset, self.index, value)

    def _deserialize(self, bin_obj, location):
        return bin_obj.read_bit(location + self.offset, self.index)

class StructField(AbstractStructField):

    def __init__(self, name, struct, offset, serializer=None,
                 deserializer=None):
        super().__init__(name, offset, serializer, deserializer)
        self.struct = struct

    def _serialize(self, bin_obj, location, values):
        self.struct.serialize(bin_obj, location, values)

    def _deserialize(self, bin_obj, location):
        return self.struct.deserialize(bin_obj, location)

class StructArrayField(AbstractArrayField):

    def __init__(self, name, struct_array, offset, serializer=None,
                 deserializer=None):
        super().__init__(name, offset, serializer, deserializer)
        self.struct_array = struct_array

    def _serialize(self, bin_obj, location, elements):
        self.struct_array.serialize(bin_obj, location, elements)

    def _deserialize(self, bin_obj, location):
        return self.struct_array.deserialize(bin_obj, location)

class Struct:

    Name   = 'Struct'
    Fields = tuple()
    Size   = 0

    @classmethod
    def serialize(cls, bin_obj, location, values):
        # assert set(values.keys()) == set([field.name for field in cls.Fields])
        for field in cls.Fields:
            field.serialize(bin_obj, location, values[field.name])

    @classmethod
    def deserialize(cls, bin_obj, location):
        return {
            field.name: field.deserialize(bin_obj, location)
            for field in cls.Fields
        }

class StructArray:

    Name = 'StructArray'
    Struct = Struct
    Count = 0

    @classmethod
    def serialize(cls, bin_obj, location, elements):
        assert len(elements) == cls.Count
        for n, element in enumerate(elements):
            location += (n * cls.Struct.Size)
            cls.Struct.serialize(bin_obj, location, element)

    @classmethod
    def deserialize(cls, bin_obj, location):
        return [
            cls.Struct.deserialize(bin_obj, location + (n * cls.Struct.Size))
            for n in range(cls.Count)
        ]

class VariantStruct:

    Name = 'VariantStruct'
    VariantField = None
    Variants = {}
    Size = 0

    @classmethod
    def serialize(cls, bin_obj, location, values):
        variant_value = values[cls.VariantField.name]
        variant = cls.Variants[variant_value]
        cls.VariantField.serialize(bin_obj, location, variant_value)
        variant.serialize(bin_obj, location, values)

    @classmethod
    def deserialize(cls, bin_obj, location):
        variant_value = cls.VariantField.deserialize(bin_obj, location)
        variant = cls.Variants[variant_value]
        values = variant.deserialize(bin_obj, location)
        values[cls.VariantField.name] = variant_value
        return values

class BinaryMapping:

    def __init__(self, field, location):
        self.field = field
        self.location = location

    def serialize(self, bin_obj, value):
        self.field.serialize(bin_obj, self.location, value)

    def deserialize(self, bin_obj):
        return self.field.deserialize(bin_obj, self.location)

class BinaryModel:

    ElementName = 'BinaryModel'
    Mappings = tuple()

    def serialize(self, instance, bin_obj):
        for mapping in self.Mappings:
            mapping.serialize(bin_obj, getattr(instance, mapping.field.name))

    def deserialize(self, instance, bin_obj):
        for mapping in self.Mappings:
            existing_value = getattr(instance, mapping.field.name, None)
            new_value = mapping.deserialize(bin_obj)
            if existing_value is None:
                existing_value = new_value
            elif mapping.field.FieldType == FieldType.Scalar:
                existing_value = new_value
            elif mapping.field.FieldType == FieldType.Struct:
                existing_value.update(new_value)
            elif mapping.field.FieldType == FieldType.Array:
                for existing, new in zip(existing_value, new_value):
                    existing.update(new)
            setattr(instance, mapping.field.name, existing_value)

class BinaryModelObject(BinaryObject, BinaryModel):

    def serialize(self):
        super().serialize(self, self)

    def deserialize(self):
        super().deserialize(self, self)
