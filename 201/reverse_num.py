#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 02:16:41 2022

@author: kali

Given an integer greater than 9, 
print all the digits in the reverse order, 
1's value first, 
and then 10's value and then the 100's value, 
and so on, with a space in between.


	1234 >> 4 3 2 1
"""


def reverse_number(num):
    return (" ".join(num[::-1]))
 

user_input = input()
print(reverse_number(user_input))