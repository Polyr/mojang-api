#!/usr/bin/env python3

from importlib import import_module

PACKAGE = 'mojang_api'
IMPORTS = {
    'authenticate_user': ['', 'servers.authserver'],
    'change_skin': ['', 'servers.api'],
    'generate_client_token': ['', 'utils.uuid'],
    'get_blocked_servers': ['', 'servers.sessionserver'],
    'get_statistics': ['', 'servers.api'],
    'get_status': ['', 'servers.status'],
    'get_user_profile': ['', 'servers.sessionserver'],
    'get_username_history': ['', 'servers.api'],
    'get_uuid': ['', 'servers.api'],
    'get_uuids': ['', 'servers.api'],
    'invalidate_access_token': ['', 'servers.authserver'],
    'refresh_access_token': ['', 'servers.authserver'],
    'reset_skin': ['', 'servers.api'],
    'signout_user': ['', 'servers.authserver'],
    'upload_skin': ['', 'servers.api'],
    'validate_access_token': ['', 'servers.authserver']
}


def parse_imports(package, imports):
    imported = {import_name: [] for import_name in imports}
    for (import_name, module_paths) in imports.items():
        for module_path in module_paths:
            split_module_path = module_path.split('.')
            package_path = '.'.join([PACKAGE] + split_module_path[:-1])
            module_name = split_module_path[-1]
            package = import_module(package_path)

            if module_name:
                module = getattr(package, module_name)
                import_ = getattr(module, import_name)
            else:
                import_ = getattr(package, import_name)

            imported[import_name].append(import_)

    return imported


def are_elements_identical(iterable):
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        return True

    return all(first is rest for rest in iterator)


def test_imports():
    imported = parse_imports(PACKAGE, IMPORTS)
    for imports in imported.values():
        assert are_elements_identical(imports)
