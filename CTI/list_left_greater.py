#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a list of numbers, 
find and print all its elements 
that are greater than their left neighbor.

@author: nat
"""

a_list = [int(str_numbers) for str_numbers in input().split()]
for i in range(1, len(a_list)):
    if a_list[i] > a_list[i-1]:
        print(a_list[i], end=' ')