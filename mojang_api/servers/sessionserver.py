#!/usr/bin/env python3

from requests import get

from .._common.endpoint import BaseURL, Endpoint
from .._common.response import APIResponse


class SessionserverEndpoint(Endpoint):
    BASE_URL = BaseURL('https://sessionserver.mojang.com')
    UUID_TO_PROFILE = '/session/minecraft/profile/{uuid}'
    BLOCKED_SERVERS = '/blockedservers'


def get_user_profile(uuid):
    response = get(SessionserverEndpoint.UUID_TO_PROFILE.url.format(uuid=uuid))
    return APIResponse.from_response(response)


def get_blocked_servers():
    response = get(SessionserverEndpoint.BLOCKED_SERVERS.url)
    return APIResponse.from_response(response)
