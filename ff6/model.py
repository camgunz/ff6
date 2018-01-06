import itertools

from abc import abstractmethod

from ff6.struct import BinaryModel, FieldType
from ff6.bin_util import BinaryObject

def _build_property(name):
    real_name = '_' + name
    def getter(self):
        value = getattr(self, real_name)
        if name in self.__overrides:
            value = self.__overrides[name].get(self.__bin_obj, value)
        return value
    def setter(self, value):
        if name in self.__overrides:
            value = self.__overrides[name].set(self.__bin_obj, value)
        setattr(self, real_name, value)
        self.__section[name] = value
    return property(getter, setter)

class Index:

    def __init__(self, array_field_path, hardcoded_values=None):
        self.array_field_path = array_field_path
        self.hardcoded_values = hardcoded_values or {}

    def get(self, obj, value):
        if value in self.hardcoded_values:
            return self.hardcoded_values[value]
        for member in self.array_field_path:
            obj = getattr(obj, member)
        if isinstance(obj, list):
            return obj[value]
        return getattr(obj, value)

    def set(self, obj, value):
        if value in self.hardcoded_values:
            return self.hardcoded_values[value]
        for member in self.array_field_path:
            obj = getattr(obj, member)
        if isinstance(obj, list):
            return obj[value]
        return getattr(obj, value)

class SplitIndex:

    def __init__(self, ranges_and_paths, hardcoded_values=None):
        self.ranges_and_paths = ranges_and_paths
        self.hardcoded_values = hardcoded_values or {}

    def get(self, obj, value):
        if value in self.hardcoded_values:
            return self.hardcoded_values[value]
        for value_range, array_field_path in self.ranges_and_paths:
            if value in value_range:
                break
        else:
            raise Exception('Value "%s" out of range' % (value))
        for member in array_field_path:
            obj = getattr(obj, member)
        if isinstance(obj, list):
            return obj[value]
        return getattr(obj, value)

    def set(self, obj, value):
        if value in self.hardcoded_values[value]:
            return self.hardcoded_values[value]
        for value_range, array_field_path in self.ranges_and_paths:
            if value in value_range:
                break
        else:
            raise Exception('Value "%s" out of range' % (value))
        for member in array_field_path:
            obj = getattr(obj, member)
        if isinstance(obj, list):
            return obj[value]
        return getattr(obj, value)

class Item:

    def __init__(self, index):
        self.index = index

def dict_to_obj(path, bin_obj, deserialized_fields, d):
    if isinstance(d, list):
        return [
            dict_to_obj(
                path + [Item(n)],
                bin_obj,
                deserialized_fields,
                element
            )
            for n, element in enumerate(d)
        ]
    elif isinstance(d, dict):
        Object = ObjClass('Obj', d.keys())
        return Object(path, bin_obj, **{
            k: dict_to_obj(path + [k], bin_obj, deserialized_fields, v)
            for k, v in d.items()
        })
    else:
        return d

class BinaryModelObject(BinaryObject, BinaryModel):

    def __init__(self, data):
        BinaryObject.__init__(self, data)
        BinaryModel.__init__(self)

    def _objs_for_path(self, path):
        objs = [self]
        for member in path:
            if member is Item:
                objs = itertools.chain(*[list(obj) for obj in objs])
            else:
                objs = [getattr(obj, member) for obj in objs]
        return objs

    def serialize(self):
        super().serialize(self, self)

    def deserialize(self):
        super().deserialize(self, self)
        obj = dict_to_obj(
            [],
            self,
            self._deserialized_fields,
            self._deserialized_fields
        )
        for name, value in obj:
            setattr(self, name, value)
        for path, override in self.Overrides:
            real_path = path[:-1]
            name = path[-1]
            for obj in self._objs_for_path(real_path):
                obj.set_override(name, override)

    def save_to_file(self, file_name):
        with open(file_name, 'wb') as fobj:
            fobj.write(self.data)

def ObjClass(type_name, field_names):
    d = {name: _build_property(name) for name in field_names}

    def __init__(self, path, bin_obj, **kwargs):
        self.__overrides = {}
        self.__path = path
        self.__bin_obj = bin_obj
        self.__fields = self.__bin_obj._deserialized_fields
        self.__section = self.__fields
        for member in path:
            if isinstance(member, Item):
                self.__section = self.__section[member.index]
            else:
                self.__section = self.__section[member]
        self.__attr_names = sorted(kwargs.keys())
        for name, value in kwargs.items():
            setattr(self, '_' + name, value)

    def __iter__(self):
        for attr_name in self.__attr_names:
            yield (attr_name, getattr(self, attr_name))

    def __repr__(self):
        return '%s(%s)' % (type(self).__name__, getattr(self, 'name', ''))

    def __getitem__(self, item):
        raise NotImplementedError()

    def __setitem__(self, item):
        raise NotImplementedError()

    def set_override(self, field_name, override):
        self.__overrides[field_name] = override

    def clear_override(self, field_name):
        del self.__overrides[field_name]

    def to_dict(self):
        return {
            attr_name: getattr(self, attr_name)
            for attr_name in self.__attr_names
        }

    def update(self, obj):
        for name, value in obj:
            setattr(self, name, value)
        self.__attr_names = sorted(list(set(
            self.__attr_names + [name for name, value in obj]
        )))

    d['__init__'] = __init__
    d['__iter__'] = __iter__
    d['__repr__'] = __repr__
    d['set_override'] = set_override
    d['clear_override'] = clear_override
    d['to_dict'] = to_dict
    d['update'] = update

    return type(type_name, tuple(), d)
