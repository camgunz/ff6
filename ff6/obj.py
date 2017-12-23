from types import MethodType

def _build_property(name):
    real_name = '_' + name
    def getter(self):
        return getattr(self, real_name)
    def setter(self, value):
        setattr(self, real_name, value)
    return property(getter, setter)

def ObjClass(type_name, field_names):
    d = {name: _build_property(name) for name in field_names}

    def __init__(self, **kwargs):
        self.__attr_names = sorted(kwargs.keys())
        for name, value in kwargs.items():
            setattr(self, '_' + name, value)

    def __iter__(self):
        for attr_name in self.__attr_names:
            yield (attr_name, getattr(self, attr_name))

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, item, value):
        setattr(self, item, value)

    def __repr__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join(['{}={}'.format(name, value) for name, value in self])
       )

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
    d['__getitem__'] = __getitem__
    d['__setitem__'] = __setitem__
    d['__repr__'] = __repr__
    d['to_dict'] = to_dict
    d['update'] = update

    return type(type_name, tuple(), d)
