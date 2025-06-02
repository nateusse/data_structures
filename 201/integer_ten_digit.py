#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 22:16:58 2022

@author: kali

Given an integer, print its tens digit.
ej 1 -> 0
1000000 -> 0
45 -> 4
"""

# input : integer
# output: ineger, 1 digit
# procedimiento: 1. Revicir number
# modular 100, y div 10
#returnar digit or str?

def ten_digit(num):
   sol = ((num%100)//10)
   return sol
input_user = int(input())    
print(ten_digit(input_user))