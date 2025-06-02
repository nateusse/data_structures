#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a collection of three intervals, 
check if they are overlapping and return
the overlapping intervals.
 
 
@author: nat
"""


def mergeIntervalII(intervals):
    intervals.sort()   
    result = [intervals[0]]  
    for interval in intervals[1:]: 
        interval_2 = result[-1]           
        if do_overlap(interval, interval_2):
            merged_front = min(interval[0], interval_2[0])
            merged_back = max(interval[1], interval_2[1])
            result[-1] = [merged_front, merged_back]
        else:
            result.append(interval)
    return result

def do_overlap(interval_1, interval_2):
    front = max(interval_1[0], interval_2[0])
    back = min(interval_1[1], interval_2[1])
    return back - front >= 0

print(mergeIntervalII([[1, 3], [4, 6], [8, 10]]))