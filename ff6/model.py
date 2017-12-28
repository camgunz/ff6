import itertools

from abc import abstractmethod

from ff6.obj import ObjClass
from ff6.struct import BinaryModel, FieldType
from ff6.bin_util import BinaryObject

def _get_section(d, path):
    for member in path:
        d = d[path]
    return d

def _get_model(name, value):
    if isinstance(value, list):
        return Array(name)
    if isinstance(value, dict):
        return Struct(name)
    return value

class AbstractModel:

    def __init__(self, name, path=None):
        self.name = name
        self.path = path or []
        self.deserialized_fields = None

    def _get_section(self):
        return _get_section(self.deserialized_fields, path)

class StructModel:

    def __init__(self, name=None, overrides=[]):
        super().__init__(name)
        self.overrides = overrides

    def __getattr__(self, attr):
        return self._get_section()[attr]

    def __setattr__(self, attr, value):
        self._get_section()[attr] = value

class ArrayModel(AbstractModel):

    def __init__(self, name, path=None, element=None):
        super().__init__(name, path)
        self.element = element

    def __getitem__(self, item):
        return self._get_section()[item]

    def __setitem__(self, item, value):
        self._get_section()[item] = value

class AbstractOverride:

    @abstractmethod
    def get(self, fields, value):
        raise NotImplementedError()

    @abstractmethod
    def set(self, fields, value):
        raise NotImplementedError()

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

class Item:
    pass

def dict_to_obj(path, bin_obj, deserialized_fields, d):
    if isinstance(d, list):
        return [
            dict_to_obj(path + [Item], bin_obj, deserialized_fields, element)
            for element in d
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

