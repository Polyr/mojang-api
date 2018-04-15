#!/usr/bin/env python3

from box import Box, BoxList


class APIResponseDict(Box):
    pass


class APIResponseList(BoxList):
    pass


class APIResponseEmpty:
    def __new__(cls, *args, **kwargs):
        return super(cls.__class__, cls).__new__(cls)

    def __init__(self, *args, **kwargs):
        pass


class APIResponse:
    _response = None

    def __new__(cls, response, *args, **kwargs):
        data = None
        try:
            data = response.json()
        except ValueError:
            instance_class = APIResponseEmpty
        else:
            if isinstance(data, dict):
                instance_class = APIResponseDict
            elif isinstance(data, list):
                instance_class = APIResponseList
            else:
                raise TypeError(
                    'response\'s JSON data must be of type \'dict\' or \'list\'')

        kwargs['camel_killer_box'] = True
        name = cls.__name__
        cls = globals()[name]
        bases = (instance_class,) + (cls,)
        dct = dict(instance_class.__dict__)
        preserved_attrs = [
            '_response',
            'response',
            '__init__'
        ]

        for attr in preserved_attrs:
            dct[attr] = cls.__dict__[attr]

        new_class = type(name, bases, dct)
        instance = new_class.__new__(
            new_class, response, data, *args, **kwargs)
        new_class.__init__(instance, response, data, *args, **kwargs)
        return instance

    def __init__(self, response, *args, **kwargs):
        self._response = response
        super(self.__class__, self).__init__(*args, **kwargs)

    @property
    def response(self):
        return self._response
