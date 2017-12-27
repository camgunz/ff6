from abc import abstractmethod

from ff6.struct import FieldType

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

class Struct:

    def __init__(self, name=None, overrides=[]):
        super().__init__(name)
        self.overrides = overrides

    def __getattr__(self, attr):
        return self._get_section()[attr]

    def __setattr__(self, attr, value):
        self._get_section()[attr] = value

class Array(AbstractModel):

    def __init__(self, name, path=None, element=None):
        super().__init__(name, path)
        self.element = element

    def __getitem__(self, item):
        return self._get_section()[item]

    def __setitem__(self, item, value):
        self._get_section()[item] = value

class Index:

    def __init__(self, array_field_name):
        self.array_field_name = array_field_name

class Item:
    pass
