#!/usr/bin/env python3

from uuid import uuid4

from requests import post

from .common import EndpointEnum, format_response

AUTHSERVER_URL = 'https://authserver.mojang.com'


class AuthserverEndpoint(EndpointEnum):
    AUTHENTICATE = '/authenticate'
    REFRESH = '/refresh'
    VALIDATE = '/validate'
    SIGNOUT = '/signout'
    INVALIDATE = '/invalidate'


AuthserverEndpoint._base_url = AUTHSERVER_URL


def generate_client_token():
    return uuid4().hex


def authenticate_user(username, password, client_token=generate_client_token()):
    payload = {
        'username': username,
        'password': password,
        'clientToken': client_token
    }
    response = post(str(AuthserverEndpoint.AUTHENTICATE), json=payload)
    return format_response(response)


def refresh_access_token(access_token, client_token):
    payload = {
        'accessToken': access_token,
        'clientToken': client_token
    }
    response = post(str(AuthserverEndpoint.REFRESH), json=payload)
    return format_response(response)


def validate_access_token(access_token, client_token=None):
    payload = {
        'accessToken': access_token
    }
    if client_token != None:
        payload['clientToken'] = client_token

    response = post(str(AuthserverEndpoint.VALIDATE), json=payload)
    return format_response(response)


def signout_user(username, password):
    payload = {
        'username': username,
        'password': password
    }
    response = post(str(AuthserverEndpoint.SIGNOUT), json=payload)
    return format_response(response)


def invalidate_access_token(access_token, client_token):
    payload = {
        'accessToken': access_token,
        'clientToken': client_token
    }
    response = post(str(AuthserverEndpoint.INVALIDATE), json=payload)
    return format_response(response)
