import re

IDENTIFIER_REGEX = re.compile(r'\W|^(?=\d)')

def to_identifier(s):
    return IDENTIFIER_REGEX.sub('_', s).lower()

class NamedElementList(list):

    def __init__(self, elements):
        super().__init__(elements)
        self.__lookup_cache = {}
        self.__initialized = True

    def __getattr__(self, attr_name):
        attr_identifier = to_identifier(attr_name)
        index = self.__lookup_cache.get(attr_identifier)
        if index is None:
            for index, element in enumerate(self):
                if to_identifier(element.name) == attr_identifier:
                    self.__lookup_cache[attr_identifier] = index
                    break
            else:
                raise AttributeError(
                    f'{type(self).__name__} has no attribute "{attr_name}"'
                )
        return self[index]

    def __setattr__(self, attr_name, attr):
        if '_NamedElementList__initialized' not in self.__dict__:
            return list.__setattr__(self, attr_name, attr)
        if not attr_name in self.__dict__:
            return super.__setattr__(self, attr_name, attr)
        index = self.__lookup_cache.get(attr_name)
        if index is None:
            for index, element in enumerate(self):
                if element.name == attr_name:
                    self.__lookup_cache[attr_name] = index
                    break
            else:
                return super().__setattr__(attr_name, attr)
        self[index] = attr
