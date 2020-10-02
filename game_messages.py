# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:24:26 2020

@author: larry
"""

import tcod as libtcod

import textwrap


class Message:
    
    def __init__(self, text, color = libtcod.white):
        self.text = text
        self.color = color
        

class MessageLog:
    
    def __init__(self, x, width, height):
        self.messages = []
        self.x = x
        self.width = width
        self.height = height
        
    def add_message(self, message):
        
        new_msg_lines = textwrap.wrap(message.text, self.width)
        
        for line in new_msg_lines:
            
            if len(self.messages) == self.height:
                del self.messages[0]
                
            self.messages.append(Message(line, message.color))