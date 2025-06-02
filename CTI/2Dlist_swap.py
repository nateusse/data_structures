#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given two integers - the number of rows m and columns n 
of m×n 2d list - and subsequent m rows of n integers, 
followed by two non-negative integers i and j less than n, 
swap the columns i and j of 2d list and print the result.
@author: nat
"""

m, n = [int(s) for s in input().split()]
a = [[int(j) for j in input().split()] for i in range(m)]
col1, col2 = [int(s) for s in input().split()]
for i in range(m):
  a[i][col1], a[i][col2] = a[i][col2], a[i][col1]
for line in a:
  print(*line)