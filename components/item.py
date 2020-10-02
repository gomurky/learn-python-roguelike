# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 20:19:17 2020

@author: larry
"""

class Item:
    
    def __init__(self, use_function = None, targeting = False, targeting_message = None,  **kwargs):
        
        self.use_function = use_function
        self.targeting = targeting
        self.targeting_message = targeting_message
        self.function_kwargs = kwargs 
        
        
        
