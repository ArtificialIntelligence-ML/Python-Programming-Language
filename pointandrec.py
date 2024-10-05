# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 06:25:12 2023

@author: pq
"""

class Point:
    """Showing a point in 2D"""
    
def print_point(p):
    print('(%g,%g)' % (p.x, p.y))
    
    

class Rectangle:
    """
    Showing a rectangle.
    attributes : width, height, corner
    """

def center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

def rectangle_size_change(rect, twidth, theight):
    rect.width += twidth
    rect.height += theight
    return

rec1 = Rectangle()
rec1.width = 50.0
rec1.height = 80.0
rec1.corner = Point()
rec1.corner.x = 0.0
rec1.corner.y = 0.0

rec1.width = rec1.width + 500
rec1.height = rec1.height + 100
