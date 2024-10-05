# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 05:33:17 2023

@author: pq
"""

w = input('Enter a word: ')
v = ['a', 'e', 'i', 'o', 'u']
found = []

for letter in w:
   if letter in v:
       if letter not in found:
           found.append(letter)
for vowel in found:
    print(vowel)   