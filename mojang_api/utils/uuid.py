#!/usr/bin/env python3

from uuid import UUID, uuid4


def generate_client_token():
    return uuid4().hex


def is_valid_uuid(uuid_string):
    try:
        UUID(uuid_string)
    except ValueError:
        return False

    return True
