# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 02:40:08 2023

@author: pq
"""

w = input('Enter a phrase: ')
v = set('aeiou')
found = v.intersection(set(w))
for vowel in found:
    print(vowel)