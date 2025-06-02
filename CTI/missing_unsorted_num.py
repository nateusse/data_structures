#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given an array nums containing n unsorted distinct numbers 
in the range [0, n], return the only number in the range that is missing from the array.

@author: nat
"""

def first_missing_positive_integer_unsorted_maxn(integers):
       have_seen = [0] * (len(integers)+1)
       for num in integers:
          have_seen[num] = 1;
       for index in range(len(have_seen)):
          if (have_seen[index]==0):
             return index;
