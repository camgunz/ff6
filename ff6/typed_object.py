from ff6 import util

class TypedObject:

    def __init__(self, **kwargs):
        attribute_names = [x[0] for x in self._attributes()]
        unrecognized_parameters = [x for x in kwargs if x not in attribute_names]
        if unrecognized_parameters:
            raise ValueError('Unrecognized parameters: %s' % (
                ', ' .join(unrecognized_parameters)
            ))
        self._validate_attributes(kwargs)
        for attribute_name, attribute_checker in self._attributes():
            param = kwargs[attribute_name]
            setattr(self, attribute_name, kwargs[attribute_name])

    @classmethod
    def _attributes(cls):
        return tuple()

    @classmethod
    def _mutually_exclusive_attributes(cls):
        return tuple()

    def _validate_attributes(self, attributes):
        util.check_only_one(attributes, self._mutually_exclusive_attributes())
        for attribute_name, attribute_checker in self._attributes():
            try:
                param = attributes[attribute_name]
            except KeyError:
                import pprint
                pprint.pprint(attributes)
                msg = 'Required parameter "%s" missing'
                raise ValueError(msg % (attribute_name)) from None
            attribute_checker(attribute_name, param)

    def __repr__(self):
        attribute_names = [x[0] for x in self._attributes()]
        return '%s(%s)' % (self.TypeName,
            ', '.join(['='.join((name, repr(getattr(self, name))))
            for name in attribute_names]))

class TypedObjectContainer:

    ObjectCount = 0
    ObjectType = object
    Name = 'TypedObjectContainer'

    def __init__(self, rom, objects):
        self._rom = rom
        self._objects = objects

    @classmethod
    def get_object_from_rom(cls, rom, n):
        return cls.ObjectType.from_rom(rom, n)

    @classmethod
    def from_rom(cls, rom):
        objects = []
        for n in range(cls.ObjectCount):
            obj = cls.get_object_from_rom(rom, n)
            if obj is None:
                raise Exception('Object %d was None' % (n))
            objects.append(obj)
        return cls(rom, objects)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self._objects[item]
        for obj in self._objects:
            if obj.name == item:
                return obj

    def __repr__(self):
        return '%s(%s)' % (self.Name,
                           ', '.join([repr(obj) for obj in self._objects]))
