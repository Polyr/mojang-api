#!/usr/bin/env python3

from attrdict import AttrDict

from enum import Enum


class BaseURL:
    def __init__(self, base_url=''):
        self._base_url = base_url

    def __get__(self, instance, owner):
        return self._base_url


class Endpoint(Enum):
    BASE_URL = BaseURL()

    def __init__(self, endpoint_uri):
        self._endpoint_uri = endpoint_uri
        self._url = self.BASE_URL + self.endpoint_uri

    @property
    def endpoint_uri(self):
        return self._endpoint_uri

    @property
    def url(self):
        return self._url

    def __str__(self):
        return self.url


class APIResponse():
    def __init__(self, response):
        self._response = response
        try:
            data = response.json()
        except ValueError:
            return

        if isinstance(data, dict):
            self._data = AttrDict(data)
        elif isinstance(data, list):
            self._data = [AttrDict(json) for json in data]
        else:
            raise TypeError(
                'response JSON must be of type \'dict\' or \'list\'')

    @property
    def response(self):
        return self._response

    @property
    def data(self):
        return self._data

    def __getattr__(self, name):
        return getattr(self.data, name)

    def __str__(self):
        return str(self.data)
