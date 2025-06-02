#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given two integers A and B.
 Print all numbers from A to B inclusively, 
 in increasing order, if A < B, 
 or in decreasing order, if A ≥ B.

@author: nat
"""

a,b = int(input()), int(input())
if a<b:
    for i in range(a,b+1): print(i, end=" ")
else:
     for i in range(a,b-1,-1): print(i, end=" ")
   