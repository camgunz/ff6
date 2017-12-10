from io import StringIO

def _value_in_range(name, val, min_val, max_val):
    val = int(val)
    return val >= min_val and val <= max_val

def _camel_to_snake(s):
    accepted_abbreviations = ('GP', 'HP', 'MP')
    sio = StringIO(s[0].lower())
    skip = False
    for n in range(len(s)):
        if skip:
            skip = False
        elif s[n:n+2] in accepted_abbreviations:
            if n != 0:
                sio.write('_')
            sio.write('%s' % (s[n:n+2].lower()))
            skip = True
        elif n == 0:
            sio.write(s[n].lower())
        elif s[n].islower():
            sio.write(s[n])
        else:
            sio.write('_%s' % (s[n].lower()))
    return sio.getvalue()

class InvalidFieldValueError(ValueError):

    def __init__(self, field, value=None):
        super().__init__('Invalid value for %s.%s: %s' % (
            field.obj.TypeName,
            field.name,
            value is not None and value or field.value
        ))

class AbstractField:

    __slots__ = (
        'obj',
        'name',
        'offset',
        'transform_incoming_binary_value',
        'transform_outgoing_binary_value',
    )

    def __init__(self, obj, name, offset,
                 transform_incoming_binary_value=None,
                 transform_outgoing_binary_value=None):
        self.obj = obj
        self.name = name
        self.offset = offset
        if transform_incoming_binary_value is None:
            transform_incoming_binary_value = lambda x: x
        if transform_outgoing_binary_value is None:
            transform_outgoing_binary_value = lambda x: x
        self.transform_incoming_binary_value = transform_incoming_binary_value
        self.transform_outgoing_binary_value = transform_outgoing_binary_value

    @property
    def rom(self):
        return self.obj.rom

    @property
    def is_set(self):
        return getattr(self.obj, self.name, None) is not None

    @property
    def _value(self):
        return getattr(self.obj, self.name)

    @_value.setter
    def _value(self, new_value):
        setattr(self.obj, self.name, new_value)

    @property
    def value(self):
        value = self._value
        if not self.check_value(value):
            raise InvalidFieldValueError(self, value)
        return value

    @value.setter
    def value(self, new_value):
        if not self.check_value(new_value):
            raise InvalidFieldValueError(self, new_value)
        self._value = new_value

    def check_value(self, value):
        return True

    @property
    def _binary_value(self):
        return self._value

    @_binary_value.setter
    def _binary_value(self, new_value):
        self._value = new_value

    @property
    def binary_value(self):
        binary_value = self._binary_value
        if not self.check_binary_value(binary_value):
            raise InvalidFieldValueError(self, binary_value)
        return self.transform_outgoing_binary_value(binary_value)

    @binary_value.setter
    def binary_value(self, new_value):
        if not self.check_binary_value(new_value):
            raise InvalidFieldValueError(self, new_value)
        self._binary_value = self.transform_incoming_binary_value(new_value)

    def check_binary_value(self, value):
        return True

    def load(self):
        raise NotImplementedError()

    def save(self):
        raise NotImplementedError()

class BaseEnumField(AbstractField):

    __slots__ = (
        'obj',
        'name',
        'enum',
        'offset',
        'transform_incoming_binary_value',
        'transform_outgoing_binary_value',
    )

    def __init__(self, obj, name, enum, offset,
                 transform_incoming_binary_value=None,
                 transform_outgoing_binary_value=None):
        super().__init__(
            obj,
            name,
            offset,
            transform_incoming_binary_value,
            transform_outgoing_binary_value
        )
        self.enum = enum

    def check_value(self, value):
        for e in self.enum:
            if value == e:
                return True
        return False

    def check_binary_value(self, value):
        for e in self.enum:
            if value == e.value:
                return True
        return False

    @property
    def _binary_value(self):
        return self.value.value

    @_binary_value.setter
    def _binary_value(self, new_value):
        self._value = self.enum(new_value)

class BitField(AbstractField):

    __slots__ = (
        'obj',
        'name',
        'bit_index',
        'offset',
        'transform_incoming_binary_value',
        'transform_outgoing_binary_value',
    )

    def __init__(self, obj, name, bit_index, offset,
                 transform_incoming_binary_value=None,
                 transform_outgoing_binary_value=None):
        super().__init__(
            obj,
            name,
            offset,
            transform_incoming_binary_value,
            transform_outgoing_binary_value
        )
        self.bit_index = bit_index

    def check_value(self, value):
        return isinstance(value, bool)

    def check_binary_value(self, value):
        return value == 0 or value == 1

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

    def load(self):
        self._binary_value = self.rom.read_bit(self.offset, self.bit_index)

    def save(self):
        self.rom.write_bit(self.offset, self.bit_index, self.value)

class NumberRangeCheckMixin:

    def check_value(self, value):
        return _value_in_range(self.name, value, self.MinValue, self.MaxValue)

    def check_binary_value(self, value):
        return _value_in_range(self.name, value, self.MinValue, self.MaxValue)

class U3HighField(NumberRangeCheckMixin, AbstractField):

    MinValue = 0
    MaxValue = 7

    def load(self):
        self.binary_value = self.rom.read_high_bits(self.offset, 3)

    def save(self):
        self.rom.write_high_bits(self.offset, 3, self.binary_value)

class U3LowField(NumberRangeCheckMixin, AbstractField):

    MinValue = 0
    MaxValue = 7

    def load(self):
        self.binary_value = self.rom.read_low_bits(self.offset, 3)

    def save(self):
        self.rom.write_low_bits(self.offset, 3, self.binary_value)

class S4HighField(NumberRangeCheckMixin, AbstractField):

    MinValue = -8
    MaxValue = 7

    def load(self):
        self.binary_value = self.rom.read_high_signed_bits(self.offset, 4)

    def save(self):
        self.rom.write_high_bits(self.offset, 4, self.binary_value)

class S4LowField(NumberRangeCheckMixin, AbstractField):

    MinValue = -8
    MaxValue = 7

    def load(self):
        self.binary_value = self.rom.read_low_signed_bits(self.offset, 4)

    def save(self):
        self.rom.write_low_bits(self.offset, 4, self.binary_value)

class U4HighField(NumberRangeCheckMixin, AbstractField):

    MinValue = 0
    MaxValue = 15

    def load(self):
        self.binary_value = self.rom.read_high_bits(self.offset, 4)

    def save(self):
        self.rom.write_high_bits(self.offset, 4, self.binary_value)

class U4LowField(NumberRangeCheckMixin, AbstractField):

    MinValue = 0
    MaxValue = 15

    def load(self):
        self.binary_value = self.rom.read_low_bits(self.offset, 4)

    def save(self):
        self.rom.write_low_bits(self.offset, 4, self.binary_value)

class U5HighField(NumberRangeCheckMixin, AbstractField):

    MinValue = 0
    MaxValue = 31

    def load(self):
        self.binary_value = self.rom.read_low_bits(self.offset, 4)

    def save(self):
        self.rom.write_low_bits(self.offset, 4, self.binary_value)

class U5LowField(NumberRangeCheckMixin, AbstractField):

    MinValue = 0
    MaxValue = 31

    def load(self):
        self.binary_value = self.rom.read_low_bits(self.offset, 5)

    def save(self):
        self.rom.write_low_bits(self.offset, 5, self.binary_value)

class U6LowField(NumberRangeCheckMixin, AbstractField):

    MinValue = 0
    MaxValue = 63

    def load(self):
        self.binary_value = self.rom.read_low_bits(self.offset, 6)

    def save(self):
        self.rom.write_low_bits(self.offset, 6, self.binary_value)

class U8Field(NumberRangeCheckMixin, AbstractField):

    MinValue = 0
    MaxValue = 255

    def load(self):
        self.binary_value = self.rom.read_byte(self.offset)

    def save(self):
        self.rom.write_byte(self.offset, self.binary_value)

class U16Field(NumberRangeCheckMixin, AbstractField):

    MinValue = 0
    MaxValue = 65535

    def load(self):
        self.binary_value = self.rom.read_short(self.offset)

    def save(self):
        self.rom.write_short(self.offset, self.binary_value)

class BattleStrField(AbstractField):

    __slots__ = (
        'obj',
        'name',
        'size',
        'offset',
        'transform_incoming_binary_value',
        'transform_outgoing_binary_value',
    )

    def __init__(self, obj, name, size, offset,
                 transform_incoming_binary_value=None,
                 transform_outgoing_binary_value=None):
        super().__init__(
            obj,
            name,
            offset,
            transform_incoming_binary_value,
            transform_outgoing_binary_value
        )
        self.size = size

    def load(self):
        self.binary_value = self.rom.read_dte_battle_string(self.offset,
                                                            self.size)

    def save(self):
        self.rom.write_dte_battle_string(self.offset, self.size,
                                         self.binary_value)

class Enum3HighField(BaseEnumField, U3HighField):
    pass

class Enum3LowField(BaseEnumField, U3LowField):
    pass

class Enum4HighField(BaseEnumField, U4HighField):
    pass

class Enum4LowField(BaseEnumField, U4LowField):
    pass

class Enum5LowField(BaseEnumField, U5LowField):
    pass

class Enum6LowField(BaseEnumField, U6LowField):
    pass

class Enum8Field(BaseEnumField, U8Field):
    pass

class BaseFlagsField(AbstractField):

    __slots__ = (
        'obj',
        'name',
        'enum',
        'offset',
        'transform_incoming_binary_value',
        'transform_outgoing_binary_value',
        'prefix',
        'suffix',
    )

    def __init__(self, obj, enum, offset,
                 transform_incoming_binary_value=None,
                 transform_outgoing_binary_value=None,
                 prefix='',
                 suffix=''):
        super().__init__(
            obj,
            enum.__name__,
            offset,
            transform_incoming_binary_value,
            transform_outgoing_binary_value
        )
        self.enum = enum
        self.prefix = prefix
        self.suffix = suffix

    def check_value(self, value):
        for e in self.enum:
            if value & e:
                value &= ~e
        return value == 0

    def check_binary_value(self, value):
        for e in self.enum:
            if value & e.value:
                value &= ~e.value
        return value == 0

    @property
    def _value(self):
        return self.enum(self._binary_value)

    @_value.setter
    def _value(self, new_value):
        self._binary_value = new_value.value

    @property
    def _binary_value(self):
        value = 0
        for e in self.enum:
            attribute_name = ''.join((
                self.prefix,
                _camel_to_snake(e.name),
                self.suffix
            ))
            attribute_value = getattr(self.obj, attribute_name)
            if attribute_value:
                value |= e.value
        return value

    @_binary_value.setter
    def _binary_value(self, new_value):
        for e in self.enum:
            attribute_name = ''.join((
                self.prefix,
                _camel_to_snake(e.name),
                self.suffix
            ))
            attribute_value = new_value & e.value != 0
            setattr(self.obj, attribute_name, attribute_value)

    @property
    def is_set(self):
        return None not in [getattr(self.obj, e.name, None) for e in self.enum]

class Flags5HighField(BaseFlagsField, U5HighField):
    pass

class Flags4HighField(BaseFlagsField, U4HighField):
    pass

class Flags4LowField(BaseFlagsField, U4LowField):
    pass

class Flags8Field(BaseFlagsField, U8Field):
    pass

class Flags16Field(BaseFlagsField, U16Field):
    pass

class TypedObject:

    def __init__(self):
        self._fields = self._build_fields()

    def _build_fields(self):
        return tuple()

    def __repr__(self):
        field_names = [f.name for x in self._fields]
        return '%s(%s)' % ( self.TypeName, ', '.join([
            '='.join((name, repr(getattr(self, name))))
            for name in field_names
        ]))

    def load(self):
        for field in self._fields:
            field.load()

    def save(self):
        for field in self._fields:
            field.save()

class FF6Object(TypedObject):

    def __init__(self, rom, number):
        self.rom = rom
        self.number = number
        super().__init__()

    def __str__(self):
        return '<%s %d: %s>' % (self.TypeName, self.number, self.name)

class TypedObjectContainer:

    ObjectCount = 0
    ObjectType = object
    Name = 'TypedObjectContainer'

    def __init__(self, rom):
        self._rom = rom
        self._objects = []

    def _get_object_from_rom(self, rom, n):
        return self.ObjectType(rom, n)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self._objects[item]
        for obj in self._objects:
            if obj.name == item:
                return obj

    def __len__(self):
        return len(self._objects)

    def __repr__(self):
        return '%s(%s)' % (
            self.Name,
            ', '.join([repr(obj) for obj in self._objects])
        )

    def load(self):
        self._objects = []
        for n in range(self.ObjectCount):
            if n in self.Blanks:
                continue
            obj = self._get_object_from_rom(self._rom, n)
            obj.load()
            self._objects.append(obj)

    def save(self):
        for obj in self._objects:
            obj.save()
