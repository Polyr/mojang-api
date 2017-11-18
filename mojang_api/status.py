#!/usr/bin/env python3

from requests import get

from .common import EndpointEnum, format_response

STATUS_URL = 'https://status.mojang.com'


class StatusEndpoint(EndpointEnum):
    CHECK = '/check'


StatusEndpoint._base_url = STATUS_URL


def get_status():
    response = get(str(StatusEndpoint.CHECK))
    return format_response(response)
