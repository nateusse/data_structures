#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chess queen moves horizontally, 
vertically or diagonally in any number of squares. 
Given two different squares of the chessboard, 
determine whether a queen can go from the 
first square to the second one in a single move.

The program receives four numbers from 1 to 8 
each specifying the column and the row number,
 first two - for the first square, 
 and the last two - for the second square. 
 The program should output YES if a queen can go 
 from the first square to the second one in a single move or NO otherwise.

@author: nat
"""

a , b, c, d = int(input()),int(input()),int(input()),int(input())
if abs(a-c)==abs(b-d):
    print("YES")
else:
    print("NO")