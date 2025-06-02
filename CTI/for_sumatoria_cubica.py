#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
For the given integer N calculate the following sum:

1³ + 2³ + ... + N³

@author: nat
"""

num = int(input())
result = 0
for i in range (num+1):
    result += i**3
print(result)
    