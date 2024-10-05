# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 05:46:49 2023

@author: pq
"""

file_name = 'data1r.txt'
try:
    with open(file_name) as f:
        contents = f.read()
        
except FileNotFoundError:
    print('The specified file is not available.')
    
else:
    words = contents.split()
    words_number = len(words)
    print(f'{file_name} file has {words_number} words.')
   
   
