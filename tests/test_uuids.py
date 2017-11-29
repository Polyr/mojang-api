#!/usr/bin/env python3

from mojang_api.apis.api import get_uuid

USERNAME_UUID_PAIRS = [
    ('Notch', '069a79f444e94726a5befca90e38aaf5'),
    ('jeb_', '853c80ef3c3749fdaa49938b674adae6'),
    ('Synchronous', '15fffb7e57c64b70bbc3a42dddaf0f81')
]


def test_uuids():
    empirical_username_uuid_pairs = [(uuid.name, uuid.id) for uuid in [get_uuid(
        username_uuid_pair[0]) for username_uuid_pair in USERNAME_UUID_PAIRS]]
    assert empirical_username_uuid_pairs == USERNAME_UUID_PAIRS
