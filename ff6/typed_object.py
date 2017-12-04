from ff6 import util

class TypedObject:

    def __init__(self, **kwargs):
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
                msg = 'Required parameter "%s" missing'
                raise ValueError(msg % (attribute_name)) from None
            attribute_checker(attribute_name, param)
