#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The first line of input contains the integer N, 
which is the number of integers to follow. 
Each of the next N lines contains one integer. 
Print the sum of these N integers.

@author: nat
"""

n = int(input())
count = 0
for i in range (n):
    count += int(input())
print(count)
