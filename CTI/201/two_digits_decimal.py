#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 21:30:59 2022

@author: kali

Given a two-digit integer, 
print its left digit (a tens digit) 
and then its right digit (a ones digit). 
Use the operator of integer division for 
obtaining the tens digit and the operator of 
taking remainder for obtaining the ones digit.

ej 79 >>  7 9
"""

# qe entra decimal numero
# que sale 2 nums
# opreacion, retornat ultimo y dividir por 10

def two_bit_integer(num):
   
   decimal = num // 10
   last = num % 10
   
   return(str(decimal)+" "+ str(last))

user_input = int(input())
print(two_bit_integer(user_input))