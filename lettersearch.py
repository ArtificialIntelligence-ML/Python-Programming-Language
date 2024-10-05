# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 02:53:20 2023

@author: pq
"""

def search_for_vowels(phrase:str) -> set:
    
    '''A function for showing the vowels inside an input word'''
    #w = input('Enter a phrase: ')
    v = set('aeiou')
     
    return v.intersection(set(phrase))
        
def search_for_letters(phrase:str, letters:str = 'aeiou') -> set:
    
    '''Return the set of letters found in phrase'''
     
    return set(letters).intersection(set(phrase))
        