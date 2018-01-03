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
    return property(getter, setter)

def ObjClass(type_name, field_names):
    d = {name: _build_property(name) for name in field_names}

    def __init__(self, path, bin_obj, **kwargs):
        self.__overrides = {}
        self.__path = path
        self.__bin_obj = bin_obj
        self.__fields = self.__bin_obj._deserialized_fields
        self.__section = self.__fields
        for member in path:
            if isinstance(member, type):
                break
            self.__section = self.__section[member]
        self.__attr_names = sorted(kwargs.keys())
        for name, value in kwargs.items():
            setattr(self, '_' + name, value)

    def __iter__(self):
        for attr_name in self.__attr_names:
            yield (attr_name, getattr(self, attr_name))

    def __repr__(self):
        return '%s(%s)' % (type(self).__name__, getattr(self, 'name', ''))

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
