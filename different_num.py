#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given three integers, in which two are equal 
to each other and the third one is different. 
Print the order number of this different one - 1, 2 or 3.

@author: nat
"""


a, b, c = int(input()),int(input()),int(input())
if (a == b and c!=b):
    print(3)
elif (a==c and b!=c):
    print(2)
else:
    print(1)