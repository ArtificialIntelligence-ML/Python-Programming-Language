# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 01:47:38 2023

@author: pq
"""

import json

def password_identificaton():

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