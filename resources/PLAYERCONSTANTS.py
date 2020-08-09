''' PLAYERCONSTANTS.py

This file contains constants for the player

'''
from enum import Enum, unique

@unique
class PLAYERCONSTANTS(Enum):
    # Player status's
    ALIVE = 0
    BUST = 1
    STOOD = 2

    # Player actions
    HIT = 3
    STAND = 4 # Not to be confused with stood, which is a player statusx   x

