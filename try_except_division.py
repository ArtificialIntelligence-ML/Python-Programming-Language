# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 05:42:40 2023

@author: pq
"""

print('Enter two numbers for division.')
print('Quite the program by entering q')

while True:
    first_number = input('\nfirst number: ')
    if first_number == 'q':
        break
    
    second_number = input('\nsecond number: ')
    if second_number == 'q':
        break
    try:
        division_output = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('Dividing number into zero is impossible.')
        
    else:
        
        print(division_output)