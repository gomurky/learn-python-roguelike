# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 14:54:42 2020

@author: larry
"""

class Tile:
    
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked
        self.explored = False
        
        
        if block_sight is None:
            block_sight = blocked
            
        self.block_sight = block_sight