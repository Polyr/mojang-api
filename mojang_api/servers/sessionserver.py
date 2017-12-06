#!/usr/bin/env python3

from requests import get

from . import api
from .._common.endpoint import BaseURL, Endpoint
from .._common.player import accept_player
from .._common.response import APIResponse


class SessionserverEndpoint(Endpoint):
    BASE_URL = BaseURL('https://sessionserver.mojang.com')
    UUID_TO_PROFILE = '/session/minecraft/profile/{uuid}'
    BLOCKED_SERVERS = '/blockedservers'


@accept_player(1)
def get_user_profile(player):
    if not player.uuid and player.username:
        player.uuid = api.get_uuid(player).id

    response = get(
        SessionserverEndpoint.UUID_TO_PROFILE.url.format(uuid=player.uuid))
    return APIResponse(response)


def get_blocked_servers():
    response = get(SessionserverEndpoint.BLOCKED_SERVERS.url)
    return APIResponse(response)
