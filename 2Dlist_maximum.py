#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given two integers - the number of rows 
m and columns n of m×n 2d list -
 and subsequent m rows of n integers, 
 find the maximal element and print its 
 row number and column number. If there 
 are many maximal elements in different rows, 
 report the one with smaller row number. 
 If there are many maximal elements in the same row, 
 report the one with smaller column number.
    if  nums[a][b] > maxi:
          maxi, max_row, max_column = nums[a][b],a,b  
print(max_row, max_column)


@author: nat
"""

m, n = [int(x) for x in input().split()]
nums = [[int(y) for y in input().split()] for s in range(m)]
maxi, max_row, max_column = nums[0][0], 0, 0
for a in range(m):
    for b in range(n):
        if  nums[a][b] > maxi:
            maxi, max_row, max_column = nums[a][b],a,b  
print(max_row, max_column)