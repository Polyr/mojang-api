#!/usr/bin/env python3

from json.decoder import JSONDecodeError

from enum import Enum


class EndpointEnum(Enum):
    @property
    def base_url(self):
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        self._base_url = base_url

    def __str__(self):
        return self.base_url + self.value


def format_response(response):
    try:
        return response.json()
    except JSONDecodeError:
        return None
