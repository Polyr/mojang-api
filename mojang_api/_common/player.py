#!/usr/bin/env python3

from functools import wraps

from ..user.player import Player
from ..utils.uuid import is_valid_uuid


def accept_player(*arg_pos_range):
    arg_pos_slice = slice(*arg_pos_range)
    arg_pos_range = [0 if arg_pos_slice.start is None else arg_pos_slice.start,
                     arg_pos_slice.stop, 1 if arg_pos_slice.step is None else arg_pos_slice.step]

    def decorator(func):
        @wraps(func)
        def with_player_acceptance(*args, **kwargs):
            args = list(args)
            if arg_pos_range[1] is None:
                arg_pos_range[1] = len(args)

            for arg_pos in range(*arg_pos_range):
                player = args[arg_pos]
                if isinstance(player, Player):
                    pass
                elif isinstance(player, str):
                    if is_valid_uuid(player):
                        args[arg_pos] = Player(uuid=player)
                    else:
                        args[arg_pos] = Player(username=player)
                else:
                    raise TypeError(
                        'player must be a valid Player, username, or UUID')

            return func(*args, **kwargs)

        return with_player_acceptance

    return decorator
