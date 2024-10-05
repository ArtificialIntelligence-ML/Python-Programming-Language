# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 07:59:11 2023

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

def correct_time(time_):
    if time_.hour < 0 or time_.minute <0 or time_.second < 0:
        return False
    elif time_.minute >= 60 or time_.second >= 60:
        return False
    else:
        return True

def print_time(t):
    """Showing string format of time.
    t :Time objec
    """
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))
    
def time_to_int(time_):
    minutes = time_.hour * 60 + time_.minute
    seconds = minutes * 60 + time_.second
    return seconds

def int_to_time(seconds):
    _time = Time()
    minutes, _time.second = divmod(seconds, 60)
    _time.hour, _time.minute = divmod(minutes, 60)
    return _time
    
def time_increase(t1, t2):
    assert correct_time(t1) and correct_time(t2)
    # if not correct_time(t1) or not correct_time(t2):
    #     raise ValueError('time object is not correct.')
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)
    # sum_ = Time()
    # sum_.hour = t1.hour +t2.hour
    # sum_.minute = t1.minute + t2.minute
    # sum_.second = t1.second + t2.second
    # if sum_.second >= 60:
    #     sum_.second -= 60
    #     sum_.minute += 1
    # if sum_.minute >= 60:
    #     sum_.minute -= 60
    #     sum_.hour += 1
    # return sum_

def increment(time_, seconds):
    time_.second += seconds
    if time_.second >= 60:
        time_.second -= 60
        time_.minute += 1
    if time_.minute >= 60:
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






