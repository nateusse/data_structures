#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given an integer greater than 9, 
print its last two bits with space in between.



@author: nat
"""

s = bin(int(input()))
print(s[-2],s[-1])