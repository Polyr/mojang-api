#!/usr/bin/env python3

from importlib import import_module

PACKAGE = 'mojang_api'
IMPORTS = [
    ('authenticate_user', 'servers.authserver'),
    ('change_skin', 'servers.api'),
    ('generate_client_token', 'utils.uuid'),
    ('get_blocked_servers', 'servers.sessionserver'),
    ('get_statistics', 'servers.api'),
    ('get_status', 'servers.status'),
    ('get_user_profile', 'servers.sessionserver'),
    ('get_username_history', 'servers.api'),
    ('get_uuid', 'servers.api'),
    ('get_uuids', 'servers.api'),
    ('invalidate_access_token', 'servers.authserver'),
    ('refresh_access_token', 'servers.authserver'),
    ('reset_skin', 'servers.api'),
    ('signout_user', 'servers.authserver'),
    ('upload_skin', 'servers.api'),
    ('validate_access_token' 'servers.authserver')
]


def test_imports():
    for (to_import, sub_package) in IMPORTS:
        assert import_module(to_import, package=PACKAGE) is import_module(
            to_import, package='{}.{}'.format(PACKAGE, sub_package))
