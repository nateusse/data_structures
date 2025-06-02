#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given two integers - the number of rows m and columns
 n of m×n 2d list - and subsequent m rows of n integers, 
 followed by one integer c. 
 Multiply every element by c and print the result.
 
11 12 13 14

21 22 23 24

31 32 33 34
 

@author: nat


"""

m, n = [int(i) for i in input().split()]
nums = [[int(x) for x in input().split()] for z in range(m)]
multi = int(input())
for a in range(m):
  for b in range(n):
    nums[a][b] *= multi  
for result in nums:
  print(*result)