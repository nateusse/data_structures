#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
For a given integer n ≤ 9 print a ladder of n steps.
 The k-th step consists of the integers from 1 to k 
 without spaces between them.

To do that, you can use the sep and end arguments for
the function print().

For example, for n = 3, your program must print,

1
12
123

@author: nat
"""

num= int(input())
if(num<=9):
  for i in range (num+1):
    for j in range(1,i+1):
      print(j,end="")
    print("")