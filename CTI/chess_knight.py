#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chess knight can move to a square that is 
two squares away horizontally and one square vertically, 
or two squares vertically and one square horizontally. 
The complete move, therefore, 
looks like the letter L. Given two different squares of the chessboard, 
determine whether a knight can go from the first square to the second one in a single move.

 

The program receives four numbers from 1 to 8 each specifying the column and the row number, 
first two - for the first square, and the last two - for the second square. 
The program should output YES if a knight can go from the 
first square to the second one in a single move or NO otherwise.

@author: nat
"""

a , b, c, d = int(input()),int(input()),int(input()),int(input())
if (c == a + 1 or c == a - 1) and (d == b - 2 or d == b + 2):
  print ("YES")
elif (d == b + 1 or d == b - 1) and (c == a - 2 or c == a + 2):
  print ("YES")
else:
  print ("NO")