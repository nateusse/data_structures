#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
"""
Created on Tue Sep 20 19:03:14 2022

@author: kali

A car can cover a distance of N kilometers per day. 
How many days will it take to cover 
a route of length M kilometers? 
The program gets two numbers: N and M.

10 999 >>100
10 1001 >> 101
10 19 >> 2


"""

def car_route(kilometers, route):
    day = route/kilometers
    return math.ceil(day)
      
    
num1, num2 = int(input()), int(input())
print(car_route(num1, num2))