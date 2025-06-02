#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a list of numbers, 
create a new list with its elements 
that are greater than their left neighbor
 and print the content of this new list.
 

 
@author: nat
"""

a_list = [int(str_numbers) for str_numbers in input().split()]
new_list = []
for i in range(1, len(a_list)):
    if a_list[i] > a_list[i-1]:
        new_list.append(a_list[i])
        
print(*new_list)