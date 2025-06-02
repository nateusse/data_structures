#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given two positive integers n and m, 
create a two-dimensional array of size 
n×m and populate it with the characters "." 
and "*" in a chequered pattern. 
The top left corner should have the character "." .



@author: nat
"""

n, m = [int(s) for s in input().split()]
a = [['.' if (i + j) % 2 == 0 else '*']
     for i in range(n)
     for j in range(m)]
for line in a:
  print(*line)