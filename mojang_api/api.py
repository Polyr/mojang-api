#!/usr/bin/env python3

from requests import delete, get, post, put

from .common import EndpointEnum, format_response

API_URL = 'https://api.mojang.com'


class APIEndpoint(EndpointEnum):
    USERNAME_TO_UUID_AT_TIME = '/users/profiles/minecraft/{username}'
    UUID_TO_USERNAME_HISTORY = '/user/profiles/{uuid}/names'
    USERNAMES_TO_UUIDS = '/profiles/minecraft'
    CHANGE_SKIN = '/user/profile/{uuid}/skin'
    UPLOAD_SKIN = '/user/profile/{uuid}/skin'
    RESET_SKIN = '/user/profile/{uuid}/skin'
    STATISTICS = '/orders/statistics'


APIEndpoint._base_url = API_URL


def get_uuid(username, timestamp=None):
    params = {
        'at': timestamp
    }
    response = get(str(APIEndpoint.USERNAME_TO_UUID_AT_TIME).format(
        username=username), params=params)
    return format_response(response)


def get_username_history(uuid):
    response = get(str(APIEndpoint.UUID_TO_USERNAME_HISTORY).format(uuid=uuid))
    return format_response(response)


def get_uuids(*usernames):
    response = post(str(APIEndpoint.USERNAMES_TO_UUIDS), json=usernames)
    return format_response(response)


def change_skin(uuid, access_token, skin_url, slim_model=False):
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    payload = {
        'model': 'slim' if slim_model else '',
        'url': skin_url
    }
    response = post(str(APIEndpoint.CHANGE_SKIN).format(
        uuid=uuid), headers=headers, data=payload)
    return format_response(response)


def upload_skin(uuid, access_token, path_to_skin, slim_model=False):
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    files = {
        'model': 'slim' if slim_model else '',
        'file': open(path_to_skin, 'rb')
    }
    response = put(str(APIEndpoint.UPLOAD_SKIN).format(
        uuid=uuid), headers=headers, files=files)
    return format_response(response)


def reset_skin(uuid, access_token):
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    response = delete(str(APIEndpoint.RESET_SKIN).format(
        uuid=uuid), headers=headers)
    return format_response(response)


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
    response = post(str(APIEndpoint.STATISTICS), json=payload)
    return format_response(response)
