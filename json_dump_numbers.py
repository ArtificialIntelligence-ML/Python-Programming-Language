# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 06:03:33 2023

@author: pq
"""

import json

numbers = [100, 200, 1, 25, 81, 123]

file_name = 'numbers.json'

with open(file_name, 'w') as f:
    json.dump(numbers, f)
    
    
with open(file_name) as f:
    json.load(f)
    print(numbers)