# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 08:49:39 2023

@author: pq
"""

def count(a):
    if a<=0:
        print('End')
    else:
        print(a)
        count(a-1)
        
def print_phrase(phrase, a):
    if a<=0:
        return
    print(phrase)
    print_phrase(phrase, a-1)
    
def factorial(n):
    if not isinstance(n, int):
        print('factorial is just defined for integers.')
        return None
    elif(n<0):
        print('factorial is not defined for negative numbers.')
        return None
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)