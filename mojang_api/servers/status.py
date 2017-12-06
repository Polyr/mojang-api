#!/usr/bin/env python3

from requests import get

from .._common.endpoint import BaseURL, Endpoint
from .._common.response import APIResponse


class StatusEndpoint(Endpoint):
    BASE_URL = BaseURL('https://status.mojang.com')
    CHECK = '/check'


def get_status():
    response = get(StatusEndpoint.CHECK.url)
    return APIResponse(response)
