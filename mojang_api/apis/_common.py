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
            json = response.json()
        except ValueError:
            return

        self._json = AttrDict(json)

    @property
    def response(self):
        return self._response

    @property
    def json(self):
        return self._json

    def __getattr__(self, name):
        return getattr(self.json, name)

    def __str__(self):
        return str(self.json)
