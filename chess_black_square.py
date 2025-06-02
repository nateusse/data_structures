#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a square of a chessboard. 
If it's a black square, print YES,
 otherwise print NO.

 

The program receives two integers from
 1 to 8 specifying the column and row 
 number of the square.
@author: nat
"""

a, b = int(input()), int(input())

if a % 2 == 0 and b % 2 == 0:
  print("YES")
elif a % 2 != 0 and b % 2 != 0:
  print("YES")
else:
  print("NO")