#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given an array/list nums containing n sorted numbers 
between -3 * 104 and 3 * 104  return the only 
number that appears once in the array/list.

@author: nat
"""

def single(nums):
    lista = []
    for i in nums:
        if i not in lista:
            lista.append(i)
        else:
           lista.remove(i)
    return lista.pop()


single([3, 1, 1])