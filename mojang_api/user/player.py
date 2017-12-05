#!/usr/bin/env python3


class Player:
    def __init__(self, username='', uuid=''):
        self._validate(username, uuid)
        self._username = username
        self._uuid = uuid

    def _validate(self, username=None, uuid=None):
        if username is None:
            username = self.username

        if uuid is None:
            uuid = self.uuid

        if not (username or uuid):
            raise AttributeError('Player must contain a username or UUID')

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if username:
            self._username = username
        else:
            del self.username

    @username.deleter
    def username(self):
        self._validate(username='')
        self._username = ''

    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        if uuid:
            self._uuid = uuid
        else:
            del self.uuid

    @uuid.deleter
    def uuid(self):
        self._validate(uuid='')
        self._uuid = ''
