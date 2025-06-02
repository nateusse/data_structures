#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a collection of two intervals, 
check if they are overlapping and return 
the overlapping intervals.

@author: nat
"""


def mergeIntervalI(intervals):
    x1 = intervals[0][0]
    x2 = intervals[0][1]
    y1 = intervals[1][0]
    y2 = intervals[1][1]
    if (y1 <= x2):
        if (y2 < x2):
            return [[x1,x2]]
        else:
            return [[x1,y2]]
    else:
        return [[x1,x2], [y1,y2]]
        
            

       