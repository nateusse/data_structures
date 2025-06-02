#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 17:19:54 2022

@author: kali


A cupcake costs A dollars and B cents.
Determine how many dollars and cents should one pay for N cupcakes. 
A program gets three numbers: A, B, N. 
It should print two numbers: total cost in dollars and cents.


Ej: 	10 15 2
return 20 30

"""


# input 3 nums, dollar, cents,amount cupckaes 
# return 2 nums, total cost dollar, total cost ,  cents
#
#
def dollar_and_cents(num1,num2, num3):
    cents_price = num2*num3 % 100
    dollar_price = num1*num3 + (num2*num3 // 100) 
    return str(dollar_price) + " " + str(cents_price)
       
    
    
    
user_input1, user_input2, user_input3   = int(input()),int(input()),int(input())
print(dollar_and_cents(user_input1, user_input2, user_input3 ))