#!/usr/bin/env python3

from mojang_api import get_uuid

from pytest import users


def test_uuids():
    empirical_users = [(uuid.name, uuid.id)
                       for uuid in [get_uuid(user[0]) for user in users]]
    assert empirical_users == users
