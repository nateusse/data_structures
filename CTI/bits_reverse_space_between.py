#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given an integer greater than 9, 
print all the bits in the reverse order, 
1's value first, and then 2's value and then 
the 4's value, and then the 8's value and so on,
 with a space in between.



@author: nat
"""

s = bin(int(input()))
result = " ".join(s[::-1])
print(result[0:-3])