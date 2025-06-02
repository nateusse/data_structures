#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 20:15:04 2022

@author: ubuntu

Given five input numbers, a, b, c, d and n, 
print out the number of 1 bits at the nth 
least significant bit position in all four
numbers a, b, c, d.
"""

def numbers_right_binary(num):
    list_nums = num.split()
    res1, res2 =  int(list_nums[0])>>int(list_nums[-1]) , int(list_nums[1])>>int(list_nums[-1])
    res3, res4 = int(list_nums[2])>>int(list_nums[-1]), int(list_nums[3])>>int(list_nums[-1])
    return (res1 + res2 ) + ( res3 +  res4) 

user = input()
print(numbers_right_binary(user))