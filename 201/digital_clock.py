#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 18:26:33 2022

@author: kali
150 >> 2 30
180 3 0

Given the integer N - the number of minutes t
hat is passed since midnight - how many hours 
and minutes are displayed on the 24h digital clock?

The program should print two numbers: 
    the number of hours (between 0 and 23) 
    and the number of minutes (between 0 and 59).

For example, if N = 150, 
then 150 minutes have passed since midnight - i.e. 
now is 2:30 am. So the program should print 2 30.
"""

def digital_clock(num):
    return str(num//60) + " "+ str( num%60)
      
    
user_input = int(input())
print(digital_clock(user_input))