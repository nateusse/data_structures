#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given an array nums containing n sorted distinct
 numbers in the range [0, n], return the only number
 in the range that is missing from the array.

@author: nat
"""


def first_missing_positive_integer_sorted(integers):
    for index in range(len(integers)):
        if (index != integers[index]):
            return index;
    return len(integers);

