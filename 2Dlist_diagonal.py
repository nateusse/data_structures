#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Given an integer n, create a two-dimensional array of size n×n 
according to the following rules and print it:

On the antidiagonal put 1.
On the diagonals above it put 0.
On the diagonals below it put 2.

@author: nat
"""

num = int(input())
box = [[0] * num for i in range(num)]
for a in range(num):
  for b in range(num):
    if a + b + 1 < num: box[a][b] = 0
    elif a + b + 1 == num: box[a][b] = 1
    else:box[a][b] = 2
for result in box:
  print(*result)