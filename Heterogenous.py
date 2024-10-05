# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 06:29:26 2023

@author: pq
"""

phrase = 'Hello, have a nice time!'
Ph_list = list(phrase)
Ph_list.pop()

for i in range(2):
    Ph_list.remove('l')
    
    
Ph_list.insert(2, Ph_list.pop(17))
Ph_list.insert(3, Ph_list.pop(9))
Ph_list.insert(4, 'r')
Ph_list.insert(6, 'g')

for i in range(8):
    Ph_list.pop(7)

Ph_list.insert(7, Ph_list.pop(10))
Ph_list.insert(8, 'o')
Ph_list.insert(9, 'u')
Ph_list.insert(10, 's')

for i in range(7):
    Ph_list.pop()
    
new_phrase = ''.join(Ph_list)

print(phrase)
print(Ph_list)
print(new_phrase)


