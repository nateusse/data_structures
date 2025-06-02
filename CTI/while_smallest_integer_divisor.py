#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given an integer not less than 2. 
Print its smallest integer divisor greater than 1.

@author: nat
"""

s = int(input())
counter = 2
while s % counter != 0:
    counter += 1
print(counter)