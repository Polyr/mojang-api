#!/usr/bin/env python3

from requests import post

from .._common.endpoint import BaseURL, Endpoint
from .._common.response import APIResponse
from ..utils.uuid import generate_client_token


class AuthserverEndpoint(Endpoint):
    BASE_URL = BaseURL('https://authserver.mojang.com')
    AUTHENTICATE = '/authenticate'
    REFRESH = '/refresh'
    VALIDATE = '/validate'
    SIGNOUT = '/signout'
    INVALIDATE = '/invalidate'


def authenticate_user(username, password, client_token=generate_client_token(), request_user=False):
    payload = {
        'agent': {
            'name': 'Minecraft',
            'version': 1
        },
        'username': username,
        'password': password,
        'clientToken': client_token
    }
    if request_user:
        payload['requestUser'] = True

    response = post(AuthserverEndpoint.AUTHENTICATE.url, json=payload)
    return APIResponse(response)


def refresh_access_token(access_token, client_token, request_user=False):
    payload = {
        'accessToken': access_token,
        'clientToken': client_token
    }
    if request_user:
        payload['requestUser'] = True

    response = post(AuthserverEndpoint.REFRESH.url, json=payload)
    return APIResponse(response)


def validate_access_token(access_token, client_token=None):
    payload = {
        'accessToken': access_token
    }
    if client_token != None:
        payload['clientToken'] = client_token

    response = post(AuthserverEndpoint.VALIDATE.url, json=payload)
    return APIResponse(response)


def signout_user(username, password):
    payload = {
        'username': username,
        'password': password
    }
    response = post(AuthserverEndpoint.SIGNOUT.url, json=payload)
    return APIResponse(response)


def invalidate_access_token(access_token, client_token):
    payload = {
        'accessToken': access_token,
        'clientToken': client_token
    }
    response = post(AuthserverEndpoint.INVALIDATE.url, json=payload)
    return APIResponse(response)
