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

    def __init__(self, name, offset, transform_out=None, transform_in=None):
        self.name = name
        self.offset = offset
        self.transform_out = transform_out
        self.transform_in = transform_in

    def __repr__(self):
        return '%s(%s, %s)' % (type(self).__name__, self.name, hex(self.offset))

    def check_serialized_value(self, value):
        return True

    def check_deserialized_value(self, value):
        return True

    @abstractmethod
    def _serialize(self, bin_obj, offset, value):
        raise NotImplementedError()

    @abstractmethod
    def _deserialize(self, bin_obj, offset):
        raise NotImplementedError()

    def serialize(self, bin_obj, offset, value):
        if not self.check_serialized_value(value):
            raise InvalidFieldValueError(self.name, value)
        if self.transform_out:
            value = self.transform_out(value)
        self._serialize(bin_obj, offset, value)

    def deserialize(self, bin_obj, offset):
        value = self._deserialize(bin_obj, offset)
        if not self.check_deserialized_value(value):
            raise InvalidFieldValueError(self.name, value)
        if self.transform_in:
            value = self.transform_in(value)
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

    def __init__(self, name, enum, offset, transform_out=None,
                 transform_in=None):
        super().__init__(name, offset, transform_out, transform_in)
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

    def _serialize(self, bin_obj, offset, value):
        bytes = value.to_bytes(self.byte_length, 'little')
        bin_obj.write_bytes(offset + self.offset, bytes)

    def _deserialize(self, bin_obj, offset):
        start = offset + self.offset
        end = start + self.byte_length
        bytes = bin_obj.data[start:end]
        return self.enum.from_bytes(bytes, 'little')

class ShortEnumFieldMixin:

    ByteSide = ByteSide.Low
    BitSize  = 0

    def _serialize(self, bin_obj, offset, value):
        value = value.value
        if self.ByteSide == ByteSide.High:
            func = bin_obj.write_high_bits
        else:
            func = bin_obj.write_low_bits
        func(offset + self.offset, self.BitSize, value)

    def _deserialize(self, bin_obj, offset):
        if self.ByteSide == ByteSide.High:
            func = bin_obj.read_high_bits
        else:
            func = bin_obj.read_low_bits
        return self.enum(func(offset + self.offset, self.BitSize))

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

    def _serialize(self, bin_obj, offset, value):
        bin_obj.write_high_bits(offset + self.offset, 3, value)

    def _deserialize(self, bin_obj, offset):
        return bin_obj.read_high_bits(offset + self.offset, 3)

class U3LowField(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = 0
    MaxValue = 7

    def _serialize(self, bin_obj, offset, value):
        bin_obj.write_low_bits(offset + self.offset, 3, value)

    def _deserialize(self, bin_obj, offset):
        return bin_obj.read_low_bits(offset + self.offset, 3)

class S4HighField(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = -8
    MaxValue = 7

    def _serialize(self, bin_obj, offset, value):
        bin_obj.write_high_bits(offset + self.offset, 4, value)

    def _deserialize(self, bin_obj, offset):
        return bin_obj.read_high_signed_bits(offset + self.offset, 4)

class S4LowField(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = -8
    MaxValue = 7

    def _serialize(self, bin_obj, offset, value):
        bin_obj.write_low_bits(offset + self.offset, 4, value)

    def _deserialize(self, bin_obj, offset):
        return bin_obj.read_low_signed_bits(offset + self.offset, 4)

class U4HighField(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = 0
    MaxValue = 15

    def _serialize(self, bin_obj, offset, value):
        bin_obj.write_high_bits(offset + self.offset, 4, value)

    def _deserialize(self, bin_obj, offset):
        return bin_obj.read_high_bits(offset + self.offset, 4)

class U4LowField(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = 0
    MaxValue = 15

    def _serialize(self, bin_obj, offset, value):
        bin_obj.write_low_bits(offset + self.offset, 4, value)

    def _deserialize(self, bin_obj, offset):
        return bin_obj.read_low_bits(offset + self.offset, 4)

class U5HighField(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = 0
    MaxValue = 31

    def _serialize(self, bin_obj, offset, value):
        bin_obj.write_low_bits(offset + self.offset, 5, value)

    def _deserialize(self, bin_obj, offset):
        return bin_obj.read_low_bits(offset + self.offset, 5)

class U5LowField(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = 0
    MaxValue = 31

    def _serialize(self, bin_obj, offset, value):
        bin_obj.write_low_bits(offset + self.offset, 5, value)

    def _deserialize(self, bin_obj, offset):
        return bin_obj.read_low_bits(offset + self.offset, 5)

class U6LowField(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = 0
    MaxValue = 63

    def _serialize(self, bin_obj, offset, value):
        bin_obj.write_low_bits(offset + self.offset, 6, value)

    def _deserialize(self, bin_obj, offset):
        return bin_obj.read_low_bits(offset + self.offset, 6)

class U8Field(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = 0
    MaxValue = 255

    def _serialize(self, bin_obj, offset, value):
        bin_obj.write_byte(offset + self.offset, value)

    def _deserialize(self, bin_obj, offset):
        value = bin_obj.read_byte(offset + self.offset)
        return value

class U16Field(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = 0
    MaxValue = 65535

    def _serialize(self, bin_obj, offset, value):
        bin_obj.write_short(offset + self.offset, value)

    def _deserialize(self, bin_obj, offset):
        value = bin_obj.read_short(offset + self.offset)
        return value

class U24Field(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = 0
    MaxValue = 16777215

    def _serialize(self, bin_obj, offset, value):
        bin_obj.write_24(offset + self.offset, value)

    def _deserialize(self, bin_obj, offset):
        return bin_obj.read_24(offset + self.offset)

class TimestampField(AbstractScalarField):

    def _serialize(self, bin_obj, offset, timestamp):
        bin_obj.write_timestamp(offset + self.offset, timestamp)

    def _deserialize(self, bin_obj, offset):
        return bin_obj.read_timestamp(offset + self.offset)

class U32Field(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = 0
    MaxValue = 4294967295

    def _serialize(self, bin_obj, offset, value):
        bin_obj.write_int(offset + self.offset, value)

    def _deserialize(self, bin_obj, offset):
        return bin_obj.read_int(offset + self.offset)

class ByteField(NumberRangeCheckMixin, AbstractScalarField):

    MinValue = 0
    MaxValue = 255

    def _serialize(self, bin_obj, offset, value):
        bin_obj.write_byte(offset + self.offset, value)

    def _deserialize(self, bin_obj, offset):
        return bin_obj.read_byte(offset + self.offset)

class StrField(AbstractScalarField):

    def __init__(self, name, offset, size=None, terminator=None,
                 translation=None, padding_byte=None, transform_out=None,
                 transform_in=None):
        assert not (size is None and terminator is None)
        assert (size is None or terminator is None)
        assert not (size is None and padding_byte is not None)
        super().__init__(name, offset, transform_out, transform_in)
        self.size = size
        self.terminator = terminator
        if translation:
            self.translation_to, self.translation_from = translation
        else:
            self.translation_to, self.translation_from = (None, None)
        self.padding_byte = padding_byte

    def _serialize(self, bin_obj, offset, value):
        value = value.encode('ascii')
        if self.translation_to:
            value = bytes([self.translation_to[chr(c)] for c in value])
        if self.padding_byte:
            value = value + (b'\xff' * (self.size - len(value)))
        if self.terminator:
            value = value + self.terminator
        bin_obj.write_bytes(offset + self.offset, value)

    def _deserialize(self, bin_obj, offset):
        if self.size:
            value = bin_obj.read_bytes(offset + self.offset, self.size)
            if self.padding_byte:
                value = value.rstrip(self.padding_byte)
        elif self.terminator:
            value = bin_obj.read_bytes_until(
                offset + self.offset,
                self.terminator
            )
        if self.translation_from:
            return ''.join([self.translation_from[index] for index in value])
        return value.decode('ascii')

###
# For maximum utility there needs to be something like PointerArrayField,
# but this will do for now.
###
class PointerField(AbstractScalarField):

    def __init__(self, name, pointer_field, target_field, offset, base=0,
                 transform_out=None, transform_in=None):
        super().__init__(name, offset, transform_out, transform_in)
        self.pointer_field = pointer_field
        self.target_field = target_field
        self.base = base

    def _serialize(self, bin_obj, offset, value):
        address = self.pointer_field.deserialize(bin_obj, offset + self.offset)
        self.target_field.serialize(bin_obj, address + self.base, value)

    def _deserialize(self, bin_obj, offset):
        address = self.pointer_field.deserialize(bin_obj, offset + self.offset)
        address += self.base
        return self.target_field.deserialize(bin_obj, address)

class BitField(AbstractScalarField):

    def __init__(self, name, index, offset, transform_out=None,
                 transform_in=None):
        super().__init__(name, offset, transform_out, transform_in)
        self.index = index

    def check_serialized_value(self, value):
        return value == 0 or value == 1

    def check_deserialized_value(self, value):
        return isinstance(value, bool)

    def _serialize(self, bin_obj, offset, value):
        bin_obj.write_bit(offset + self.offset, self.index, value)

    def _deserialize(self, bin_obj, offset):
        return bin_obj.read_bit(offset + self.offset, self.index)

class StructField(AbstractStructField):

    def __init__(self, name, fields, offset, transform_out=None,
                 transform_in=None):
        super().__init__(name, offset, transform_out, transform_in)
        self.fields = fields

    def __repr__(self):
        return '%s(%s, %s, %s)' % (
            type(self).__name__,
            self.name,
            hex(self.offset),
            ', '.join([repr(field) for field in self.fields])
       )

    def _serialize(self, bin_obj, offset, values):
        for field in self.fields:
            field.serialize(bin_obj, offset + self.offset, values[field.name])

    def _deserialize(self, bin_obj, offset):
        return {
            field.name: field.deserialize(bin_obj, offset + self.offset)
            for field in self.fields
        }

class ArrayField(AbstractArrayField):

    def __init__(self, name, count, element_field, element_size, offset,
                 transform_out=None, transform_in=None):
        super().__init__(name, offset, transform_out, transform_in)
        self.count = count
        self.element_field = element_field
        self.element_size = element_size

    def __repr__(self):
        return '%s(%s, %s, %r)' % (
            type(self).__name__,
            self.name,
            hex(self.offset),
            self.element_field
        )

    def _serialize(self, bin_obj, offset, elements):
        assert len(elements) == self.count
        for n, element in enumerate(elements):
            self.element_field.serialize(
                bin_obj,
                offset + self.offset + (n * self.element_size),
                element
            )

    def _deserialize(self, bin_obj, offset):
        return [
            self.element_field.deserialize(
                bin_obj,
                offset + self.offset + (n * self.element_size)
            )
            for n in range(self.count)
        ]

class VariantField(AbstractStructField):

    def __init__(self, name, field, variants, offset, transform_out=None,
                 transform_in=None):
        super().__init__(name, offset, transform_out, transform_in)
        self.field = field
        self.variants = variants

    def _serialize(self, bin_obj, offset, values):
        location = offset + self.offset
        variant_value = values[self.field.name]
        self.field.serialize(bin_obj, location, variant_value)
        self.variants[variant_value].serialize(bin_obj, location, values)

    def _deserialize(self, bin_obj, offset):
        location = offset + self.offset
        variant_value = self.field.deserialize(bin_obj, location)
        values = self.variants[variant_value].deserialize(bin_obj, location)
        values[self.field.name] = variant_value
        return values

class BinaryModel:

    Fields = tuple()

    def serialize(self, instance, bin_obj):
        for field in self.Fields:
            field.serialize(bin_obj, 0, getattr(instance, field.name))

    def deserialize(self, instance, bin_obj):
        for field in self.Fields:
            existing_value = getattr(instance, field.name, None)
            new_value = field.deserialize(bin_obj, 0)
            if existing_value is None:
                existing_value = new_value
            elif field.FieldType == FieldType.Scalar:
                existing_value = new_value
            elif field.FieldType == FieldType.Struct:
                existing_value.update(new_value)
            elif field.FieldType == FieldType.Array:
                for existing, new in zip(existing_value, new_value):
                    existing.update(new)
            setattr(instance, field.name, existing_value)

class BinaryModelObject(BinaryObject, BinaryModel):

    def serialize(self):
        super().serialize(self, self)

    def deserialize(self):
        super().deserialize(self, self)
