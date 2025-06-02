#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a list of numbers, 
print all its even elements. 
Use a for-loop that iterates over 
the list itself and not over its indices. 
That is, don't use range().

@author: nat

11 23 5 23 64 22 11 24

lista = list(input())
even = 0
i= 0
for i in lista:
    print(i if i % 2 ==0 else "")

"""
a_list = [int(str_numbers) for str_numbers in input().split()]

for num in a_list :
   if (float(num) % 2 == 0):
      print(num, end = " ")