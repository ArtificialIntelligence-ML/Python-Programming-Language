# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 05:56:05 2023

@author: pq
"""

def words_numbers_counting(file_name):
    try:
        with open(file_name) as f:
            contents = f.read()
            
    except FileNotFoundError:
        # print('The specified file is not available.')
        pass
    else:
        words = contents.split()
        words_number = len(words)
        print(f'{file_name} file has {words_number} words.')
       