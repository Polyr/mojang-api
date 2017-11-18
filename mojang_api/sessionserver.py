#!/usr/bin/env python3

from requests import get

from .common import EndpointEnum, format_response

SESSIONSERVER_URL = 'https://sessionserver.mojang.com'


class SessionserverEndpoint(EndpointEnum):
    UUID_TO_PROFILE = '/session/minecraft/profile/{uuid}'
    BLOCKED_SERVERS = '/blockedservers'


SessionserverEndpoint._base_url = SESSIONSERVER_URL


def get_user_profile(uuid):
    response = get(
        str(SessionserverEndpoint.UUID_TO_PROFILE).format(uuid=uuid))
    return format_response(response)


def get_blocked_servers():
    response = get(str(SessionserverEndpoint.BLOCKED_SERVERS))
    return format_response(response)
