#!/usr/bin/env python3

from uuid import uuid4


def generate_client_token():
    return uuid4().hex
