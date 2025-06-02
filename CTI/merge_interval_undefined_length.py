#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a collection of intervals of any length, 
check if they are overlapping and return 
the overlapping intervals.

@author: nat
"""


def mergeIntervalIII(intervals):
    intervals.sort()   
    result = [intervals[0]]  
    for i1 in intervals[1:]: 
        i2 = result[-1]  
        first = max(i1[0], i2[0])
        last = min(i1[1], i2[1])
        if last - first >= 0:
            merged_front = min(i1[0], i2[0])
            merged_back = max(i1[1], i2[1])
            result[-1] = [merged_front, merged_back]
        else:
            result.append(i1)
    return result

print(mergeIntervalIII([[-5, 5], [2, 8], [4, 18], [15, 21]]))



'''
class Solution:
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        new_list = []
        for i in intervals:
            if not new_list  or new_list [-1][1] < i[0]:
                new_list .append(i)
            else:
                new_list [-1][1] = max(new_list [-1][1], i[1])

        return new_list 
    
    
    '''