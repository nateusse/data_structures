#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 01:18:53 2022

@author: kali


Given a 2 bit integer,
 print its last two bits in reverse order, 
 print 1's bit first and then 2's bit. 
 Use the operator of integer division 
 for obtaining the 2's bit and the operator
 of taking remainder for obtaining the ones bit.
"""

def two_bit_integer_reverse(num):
   
   first_bit = num // 2
   second_bit = num % 2
   
   return(str(second_bit) +" "+ str(first_bit))

user_input = int(input())
print(two_bit_integer_reverse(user_input))