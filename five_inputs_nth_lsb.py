#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given five input numbers, a, b, c, d and n, 
print out the number of 1 bits at the nth least 
significant bit position in all four numbers a, b, c, d.


@author: nat
"""

a = int(input()) #0010
b = int(input()) #0011
c = int(input()) #0101
d = int(input()) #0110
n = int(input()) 
bin_value1 = a >> n
bin_value2 = b >> n
bin_value3 = c >> n
bin_value4 = d >> n
sum_values = bin_value1 + bin_value2 + bin_value3 + bin_value4
print(sum_values)
