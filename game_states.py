# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 11:33:36 2020

@author: larry
"""

from enum import Enum, auto

class GameStates(Enum):    
    PLAYERS_TURN = auto()
    ENEMY_TURN = auto()
    PLAYER_DEAD = auto()
    SHOW_INVENTORY = auto()
    DROP_INVENTORY = auto()
    TARGETING = auto()
    LEVEL_UP = auto()
    CHARACTER_SCREEN = auto()