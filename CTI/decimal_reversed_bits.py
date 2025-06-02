#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given an integer greater than 9, 
print the number created by reversing the bits.
 Combine the reversed bits to create the decimal 
 value represented by the reversed bits and print 
 the decimal value.

@author: nat


"""


n = int(input())
rev = 0
while (n > 0) :
        rev = rev << 1
        if (n & 1 == 1) :
            rev = rev ^ 1
        n = n >> 1
    
print( rev)




