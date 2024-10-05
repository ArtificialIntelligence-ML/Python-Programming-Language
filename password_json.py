# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 06:08:12 2023

@author: pq
"""

import json

password = input('Enter password: ')

file_name = 'password.json'

with open(file_name, 'w') as f:
    json.dump(password, f)
    print(f'Specified password by you: {password}')
    
    
with open(file_name) as f:
    json.load(f)
    print(f'Your password was {password}')