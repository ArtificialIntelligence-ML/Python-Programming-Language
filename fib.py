# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 09:17:58 2023

@author: pq
"""

def fibonacci(n:int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)