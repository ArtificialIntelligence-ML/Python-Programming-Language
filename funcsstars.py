# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 09:22:40 2023

@author: pq
"""

def func1(*args):
    for arg in args:
        print(arg)
        
def func2(**kwargs):
    for k,v in kwargs.items():
        print('%s == %s' %(k,v))

def func3(arg1, arg2, arg3):
    print('arg1', arg1)
    print('arg2', arg2)
    print('arg3', arg3)

def average(first, *others):
    return (first + sum(others))/(1+len(others))

