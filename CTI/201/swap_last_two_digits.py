#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 01:35:49 2022

@author: kali

Given an integer greater than 9, 
print a new number that has the 
two digits in the reverse order, 
1's value first, and then 10's value.

Ej: 	567	>> 76
"""



def swap_order_two_digits(num):
   last = num%10
   last_before =num % 100
   last_final = last_before//10
   return str(last) + "" + str(last_final )
user_input = int(input())
print(swap_order_two_digits(user_input))