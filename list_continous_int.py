#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a list of non-zero integers,
 find and print the first adjacent pair of elements 
 that have the same sign. If there is no such pair, print 0.

@author: nat
"""


a_list = [int(str_numbers) for str_numbers in input().split()]
for i in range(1, len(a_list)):
  if a_list[i] * a_list[i-1] > 0:
    print(str(a_list[i - 1]), str(a_list[i]))
    break
  elif i == len(a_list)-1:
    print("0")

