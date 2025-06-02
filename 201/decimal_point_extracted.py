#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 20:06:05 2022

@author: kali

Given a positive real number, 
print its first digit to the right 
of the decimal point without using string operations.

Ej: 45.12 -> 12 , 101 -> 0
"""


# input num float, variuos decimals each time
# output one num
#procedment.
# extract only decimal, exptract second place
def decimal_extracted(num):
    decimals = num / 0.1
    digit = (decimals % 10) 
    return int(digit)
  
    
       
    
    
    
user_input = float(input())
print(decimal_extracted(user_input))