#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In mathematics, the factorial of an integer n, 
denoted by n! is the following product:

n! = 1 × 2 × … × n

For the given integer n calculate the value n!. 
Don't use the math module in this exercise.

@author: nat
"""

n = int(input())
res = 1
for i in range (1, n+1):
    res *= i
print (res)