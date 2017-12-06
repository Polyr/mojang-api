#!/usr/bin/env python3

from requests import delete, get, post, put

from . import sessionserver
from .._common.endpoint import BaseURL, Endpoint
from .._common.player import accept_player
from .._common.response import APIResponse


class APIEndpoint(Endpoint):
    BASE_URL = BaseURL('https://api.mojang.com')
    USERNAME_TO_UUID_AT_TIME = '/users/profiles/minecraft/{username}'
    UUID_TO_USERNAME_HISTORY = '/user/profiles/{uuid}/names'
    USERNAMES_TO_UUIDS = '/profiles/minecraft'
    CHANGE_SKIN = '/user/profile/{uuid}/skin'
    UPLOAD_SKIN = '/user/profile/{uuid}/skin'
    RESET_SKIN = '/user/profile/{uuid}/skin'
    STATISTICS = '/orders/statistics'


@accept_player(1)
def get_uuid(player, timestamp=None):
    if not player.username and player.uuid:
        player.username = sessionserver.get_user_profile(player).name

    params = {
        'at': timestamp
    }
    response = get(APIEndpoint.USERNAME_TO_UUID_AT_TIME.url.format(
        username=player.username), params=params)
    return APIResponse(response)


@accept_player(1)
def get_username_history(player):
    if not player.uuid and player.username:
        player.uuid = get_uuid(player).id

    response = get(
        APIEndpoint.UUID_TO_USERNAME_HISTORY.url.format(uuid=player.uuid))
    return APIResponse(response)


@accept_player(None)
def get_uuids(*players):
    usernames = []
    for player in players:
        if not player.username and player.uuid:
            player.username = sessionserver.get_user_profile(player).name

        usernames.append(player.username)

    response = post(APIEndpoint.USERNAMES_TO_UUIDS.url, json=usernames)
    return APIResponse(response)


@accept_player(1)
def change_skin(player, access_token, skin_url, slim_model=False):
    if not player.uuid and player.username:
        player.uuid = get_uuid(player).id

    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    payload = {
        'model': 'slim' if slim_model else '',
        'url': skin_url
    }
    response = post(APIEndpoint.CHANGE_SKIN.url.format(
        uuid=player.uuid), headers=headers, data=payload)
    return APIResponse(response)


@accept_player(1)
def upload_skin(player, access_token, path_to_skin, slim_model=False):
    if not player.uuid and player.username:
        player.uuid = get_uuid(player).id

    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    files = {
        'model': 'slim' if slim_model else '',
        'file': open(path_to_skin, 'rb')
    }
    response = put(APIEndpoint.UPLOAD_SKIN.url.format(
        uuid=player.uuid), headers=headers, files=files)
    return APIResponse(response)


@accept_player(1)
def reset_skin(player, access_token):
    if not player.uuid and player.username:
        player.uuid = get_uuid(player).id

    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    response = delete(APIEndpoint.RESET_SKIN.url.format(
        uuid=player.uuid), headers=headers)
    return APIResponse(response)


def get_statistics(item_sold_minecraft=False, prepaid_card_redeemed_minecraft=False, item_sold_cobalt=False, item_sold_scrolls=False):
    sales_mapping = {
        'item_sold_minecraft': item_sold_minecraft,
        'prepaid_card_redeemed_minecraft': prepaid_card_redeemed_minecraft,
        'item_sold_cobalt': item_sold_cobalt,
        'item_sold_scrolls': item_sold_scrolls
    }
    payload = {
        'metricKeys': [k for (k, v) in sales_mapping.items() if v]
    }
    response = post(APIEndpoint.STATISTICS.url, json=payload)
    return APIResponse(response)
