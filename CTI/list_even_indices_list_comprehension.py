#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a list of numbers,
 create a new list of elements with even indices 
 (i.e. A[0], A[2], A[4], ...) 
 using list comprehension and print the 
 content of this new list.

@author: nat
"""

a_list = [int(str_numbers) for str_numbers in input().split()]
new_list = [i for i in a_list[0:len(a_list):2] ]
print(*new_list)
