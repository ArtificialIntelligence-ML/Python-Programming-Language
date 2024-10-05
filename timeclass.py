# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 06:49:32 2023

@author: pq
"""

class Time:
    """
    Showing the time of a day.
    attributes: hour, minute, second
    """
time_ = Time()
time_.hour = 8
time_.minute = 45
time_.second = 12

def print_time(t):
    """Showing string format of time.
    t :Time objec
    """
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))
    
def time_increase(t1, t2):
    sum_ = Time()
    sum_.hour = t1.hour +t2.hour
    sum_.minute = t1.minute + t2.minute
    sum_.second = t1.second + t2.second
    if sum_.second >= 60:
        sum_.second -= 60
        sum_.minute += 1
    if sum_.minute >= 60:
        sum_.minute -= 60
        sum_.hour += 1
    return sum_

def increment(time_, seconds):
    time_.seconds += seconds
    while time_.second >= 60:
        time_.second -= 60
        time_.minute += 1
    while time_.minute >= 60:
        time_.minute -= 60
        time_.hour += 1
        
    return time_

start = Time()
start.hour = 8
start.minute = 45
start.second = 50

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 40

end = time_increase(start, duration)
print_time(end)