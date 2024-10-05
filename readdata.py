# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 07:33:47 2023

@author: pq
"""
file_name = 'data1.txt'
with open(file_name) as f:
    lines = f.readlines()
   
   
for line in lines:
    print(line)