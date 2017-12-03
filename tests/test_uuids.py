#!/usr/bin/env python3

from mojang_api import get_uuid

from .testing_constants import USERS


def test_uuids():
    empirical_users = [(uuid.name, uuid.id) for uuid in [get_uuid(user[0]) for user in USERS]]
    assert empirical_users == USERS
