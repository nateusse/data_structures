#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 22:23:47 2022

@author: kali

Given a three-digit number. 
Find the sum of its digits
 without using string operations.
"""

#Are those nubmer from 1, are decimals

# input integer outup sum int
#procedmiento while len extract num y sum
#return total

def sum_digits(num):
    count = len(num)
    while count != 0:
        digit = int(num)//100  + (int(num)%100)//10  + int(num)%10
        count = count - 1
        return digit
      
    
       
    
    
    
user_input = input()
print(sum_digits(user_input))

