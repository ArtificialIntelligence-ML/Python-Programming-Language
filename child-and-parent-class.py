# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:42:38 2023

@author: pq
"""

class Person:
    def __init__(self, first_name, last_name, experience):
        self.first_name = first_name
        self.last_name = last_name
        
    def print_name(self):
        print(self.first_name, self.last_name)
        
class DataScientist(Person):
    def __init__(self, first_name, last_name, experience):
        super().__init__(first_name, last_name, experience)
        self.experience = experience
    
    def print_data_scientist(self):
        print( self.first_name, self.last_name, self.experience)