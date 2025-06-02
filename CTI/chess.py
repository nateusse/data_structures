#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chess rook moves horizontally or vertically.
 Given two different squares of the chessboard, 
 determine whether a rook can go from the first square to the second one in a single move.

 

The program receives four numbers from 1 to 8 each specifying the column and the row number, 
first two - for the first square, and the last two - for the second square. 
The program should output YES if a rook can go from 
the first square to the second one in a single move or NO otherwise.

@author: nat
"""

a, b, c, d = int(input()),int(input()),int(input()), int(input())
print ("YES" if(a-c)*(b-d)==0 else "NO" )

