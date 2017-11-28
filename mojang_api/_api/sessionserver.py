#!/usr/bin/env python3

from requests import get

from ._common import BaseURL, Endpoint, format_response

SESSIONSERVER_URL = 'https://sessionserver.mojang.com'


class SessionserverEndpoint(Endpoint):
    BASE_URL = BaseURL(SESSIONSERVER_URL)
    UUID_TO_PROFILE = '/session/minecraft/profile/{uuid}'
    BLOCKED_SERVERS = '/blockedservers'


def get_user_profile(uuid):
    response = get(SessionserverEndpoint.UUID_TO_PROFILE.url.format(uuid=uuid))
    return format_response(response)


def get_blocked_servers():
    response = get(SessionserverEndpoint.BLOCKED_SERVERS.url)
    return format_response(response)
