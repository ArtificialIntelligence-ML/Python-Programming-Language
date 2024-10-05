# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 01:55:56 2023

@author: pq
"""

import json

def showing_saved_password():
    'Shows saved passwords.'
    file_name = 'password.json'
    try:
        with open(file_name) as f:
            password = json.load(f)
            
    except FileNotFoundError:
        return None
    
    else:
        return password
    
def password_identification():
    'identifies the entered password.'
    password = showing_saved_password()
    if password:
        print(f'Your password was {password}.')
        
    else:
        password = input('Enter password: ')
        file_name = 'password.json'
        with open(file_name, 'w') as f:
            json.dump(password, f)
            print(f'Specified password by you: {password}')