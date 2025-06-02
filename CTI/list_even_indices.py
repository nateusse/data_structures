#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a list of numbers, 
find and print all its elements with even indices 
(i.e. A[0], A[2], A[4], ...).

@author: nat



9 4 5 2 0


"""

a_list = [int(str_numbers) for str_numbers in input().split()]
res= a_list[0:len(a_list):2]
print(*res)

