#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 01:22:43 2022

@author: kali

Given a two-digit integer,
 swap its digits and print the result.
"""

def swap_order_two_digits(num):
   
   first_bit = num // 10
   second_bit = num % 10
   
   return(str(second_bit) +""+ str(first_bit) )

user_input = int(input())
print(swap_order_two_digits(user_input))