#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 20:41:48 2022

@author: kali

Write a program that reads an integer 
number and prints its previous and next 
numbers. See the example below.

179
The next number for the number 179 is 180
The previous number for the number 179 is 178
"""

#received num as integer, 
#return next and prevous, no float
#concatenar str
#how to print? next line

def next_and_previus_number(num):  
    next =num+1
    previus = num-1
    return "The next number for the number " + str(num) +" is "+ str(next) +  "\nThe previous number for the number " + str(num) +" is "+ str(previus)
    

user_input = int(input())
print(next_and_previus_number(user_input))