#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given integer coordinates of three vertices of a rectangle whose 
sides are parallel to coordinate axes, find the coordinates of the fourth vertex of the rectangle. 

@author: nat
"""

a1,a2,b1,b2,c1,c2 = int(input()),int(input()),int(input()),int(input()),int(input()), int(input())
if a1 == b1:
  d1 = c1
elif b1 == c1:
  d1 = a1
else:
  d1 = b1

if a2 == b2:
  d2 = c2
elif b2 == c2:
  d2 = a2
else:
  d2 = b2
print (d1)
print(d2)
