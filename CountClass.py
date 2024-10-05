# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 07:12:19 2023

@author: pq
"""

class Count:
    def __init__(self, v :int = 0, i :int = 1) -> None:
        self.val = v
        self.incr = i
    
    def __repr__(self) -> str:
        return str(self.val)
    
    def increase(self) -> None:
        self.val += self.incr