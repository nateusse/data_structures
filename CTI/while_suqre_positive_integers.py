#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
For a given integer N, 
print all the squares of positive integers 
where the square is less than or equal to N, 
in ascending order.

print([i**2 for i in range(1,s+1) if i**2 <= s])

@author: nat
"""

s =int(input())
i = 1
while i**2 <= s:
     result = i**2
     print(result, end=" ")
     i+=1


