#!/usr/bin/env python3

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
