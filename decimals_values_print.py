#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Civen an integer greater than 9, 
print all the digits in the reverse order, 
1's value first, and then 10's 
value and then the 100's value, and so on, 
with a space in between.


@author: nat


s = int(input())
reversa = 0
while(s > 0):
    a = s % 10
    reversa = reversa * 10 + a
    s = s // 10
print(" ".join(str(reversa)))
"""





s = list(input())
s.reverse()
print(' '.join(s))
 

