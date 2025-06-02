#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In mathematics, the factorial of an integer n,
 denoted by n! is the following product:

n! = 1 × 2 × … × n

For the given integer n calculate the value

1! + 2! + 3! + ... + n!

Try to discover the solution that 
uses only one for-loop. And don't use 
the math module in this exercise.

@author: nat
"""

n = int(input())
res,suma = 1,0
for i in range(1,n+1):
    res *= i 
    suma += res
print(suma)