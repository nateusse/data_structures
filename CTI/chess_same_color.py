#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given two squares of a chessboard. 
If they are painted in the same color, 
print YES, otherwise print NO.


The program receives four integers from 1 to 8, 
each specifying the column and row number, 
first two - for the first square, and then the last two - for the second square.

@author: nat
"""
a , b, c, d = int(input()),int(input()),int(input()),int(input())
if (a + b) % 2 == (c + d) % 2:
    print("YES")
else:
    print("NO")