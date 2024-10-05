# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 06:30:12 2023

@author: pq
"""

def search_for_vowels(word):
    
    '''A function for showing the vowels inside an input word'''
    #w = input('Enter a phrase: ')
    v = set('aeiou')
    found = v.intersection(set(word))
    return found
        