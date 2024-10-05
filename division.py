# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 05:30:10 2023

@author: pq
"""

# try:
#     print(100/0)
    
# except ZeroDivisionError:
#     print('Division to zero is impossible.')
    
print('Enter two numbers for division.')
print('Quite the program by entering q')

while True:
    first_number = input('\nfirst number: ')
    if first_number == 'q':
        break
    
    second_number = input('\nsecond number: ')
    if second_number == 'q':
        break
    
    division_output = int(first_number) / int(second_number)
    
    print(division_output)