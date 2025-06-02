#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a sequence of non-negative integers, 
where each number is written (input) in a separate line. 
The sequence ends with 0. Print the average of the sequence. 

@author: nat
"""

s , total, count  = int(input()), 0, 0
while s != 0:
  
  total += s
  s = int(input())
  count += 1

print(total/count)


