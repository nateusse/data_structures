#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
For a given integer X, 
find the greatest integer n where 2ⁿ 
is less than or equal to X. 
Print the exponent value and the result of the expression 2ⁿ.

@author: nat
"""

x = int(input())
i= 2
power = 1
while i <= x:
    i *= 2
    power += 1
print(power - 1,i // 2)