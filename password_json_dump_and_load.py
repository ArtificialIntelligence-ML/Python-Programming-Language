# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 06:14:39 2023

@author: pq
"""

import json

file_name = 'password.json'

try:
    with open(file_name) as f:
        password = json.load(f)
        
except FileNotFoundError:
    password = input('Enter password: ')
    file_name = 'password.json'
    with open(file_name, 'w') as f:
        json.dump(password, f)
        print(f'Specified password by you: {password}')
        
else:
    print(f'Your password was {password}')