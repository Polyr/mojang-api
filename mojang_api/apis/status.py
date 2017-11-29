#!/usr/bin/env python3

from requests import get

from ._common import APIResponse, BaseURL, Endpoint

STATUS_URL = 'https://status.mojang.com'


class StatusEndpoint(Endpoint):
    BASE_URL = BaseURL(STATUS_URL)
    CHECK = '/check'


def get_status():
    response = get(StatusEndpoint.CHECK.url)
    return APIResponse(response)
