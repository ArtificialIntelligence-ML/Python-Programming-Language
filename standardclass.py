# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:01:23 2023

@author: pq
"""

class Time:
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def __add__(self, other):
        if isinstance(other, Time):
        # seconds = self.time_to_int() + other.time_to_int()
        # return self.int_to_time(seconds)
            return self.time_increase(other)
        else:
            return self.increment(other)
        
    def __radd__(self, other):
        return self.__add__(other)
    
    def time_increase(self, other):
        
        seconds = self.time_to_int() + other.time_to_int()
        return self.int_to_time(seconds)
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))
        
    def increment(self, seconds):
        seconds += self.time_to_int()
        return self.int_to_time(seconds)
    
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def int_to_time(self, seconds):
        self = Time()
        minutes, self.second = divmod(seconds, 60)
        self.hour, self.minute = divmod(minutes, 60)
        return self
    
    def later(self, other):
        return self.time_to_int() > other.time_to_int()
    
    
        