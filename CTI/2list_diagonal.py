#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given an integer n, create a two-dimensional array o
f size n×n according to the following rules and print it:

On the main diagonal put 0.
On the diagonals adjacent to the main put 1.
On the next adjacent diagonals put 2, and so forth.

@author: nat
"""

num = int(input())
box = [[0] * num for i in range(num)]
for a in range(num):
  for b in range(num):
    box[a][b] = abs(a - b)
for result in box:
  print(*result)