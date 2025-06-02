#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given an integer greater than 9, 
print the decimal value of last two bits in reverse order.

 

@author: nat
"""


s = bin(int(input()))
print(int(s[-1]+s[-2],2))