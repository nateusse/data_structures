#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chess king moves one square in any direction.
 Given two different squares of the chessboard, 
 determine whether a king can go from the first 
 square to the second one in a single move.


The program receives four numbers from 1 to 8 
each specifying the column and the row number, 
first two - for the first square, and the last two - for the second square. 
The program should output YES if a king can go 
from the first square to the second one in a single move or NO otherwise.

@author: nat
"""

a , b, c, d = int(input()),int(input()),int(input()),int(input())
if (a == c + 1 or a == c - 1 or a == c) and (b == d + 1 or b == d - 1 or b == d):
    print ("YES")
else:
    print ("NO")