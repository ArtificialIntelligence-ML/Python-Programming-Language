# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 05:49:05 2023

@author: pq
"""

w = input('Enter a word: ')
v = ['a', 'e', 'i', 'o', 'u']
found = {}


for letter in w:
    if letter in v:
        found.setdefault(letter, 0)
        
        found[letter] += 1

for k, v in found.items():
    print(k, 'was found', v, 'time(s).') 