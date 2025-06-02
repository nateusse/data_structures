#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a list of numbers, 
create a new list of all
even elements using list 
comprehension and print the 
content of this new list.

@author: nat
"""

a_list = [int(str_numbers) for str_numbers in input().split()]
new_list = []
for num in a_list :
   if (float(num) % 2 == 0):
      new_list.append(num)
print(*new_list)