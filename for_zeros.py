#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given N numbers: the first number in the input is N,
 after that N integers are given.
 Count the number of zeros among the given 
 integers and print it.

You need to count the number of numbers 
that are equal to zero, not the number of zero digits.

@author: nat
"""

n = int(input())
count,zeros = 0,0
for i in range (1,n+1):
    count = int(input())
    if count == 0:
        zeros +=1
print(zeros)