''' PLAYERCONSTANTS.py

This file contains constants for the player
A enum module was used to replicate enums similar to javas.
'''
from enum import Enum, unique

@unique
class PLAYERCONSTANTS(Enum):
    #
    CURRENT_TURN = 1

    # Player status. Linked to ENTITY CLASS. FOR MODEL!
    ALIVE = 2
    BUST = 3
    STOOD = 4
    WIN = 7

    # Player actions. Linked to VIEW CLASS. FOR VIEW!
    HIT = 5
    STAND = 6 # Not to be confused with stood, which is a player statusx   x


