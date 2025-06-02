#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 18:34:35 2022

@author: kali

The hour hand of an analog clock turned 
α degrees since the midnight. 
Determine and print the angle by which
 the minute hand turned since the start of the current hour. 
 Input and output in this problems are integers.
 
 1 >> 12
 300 > 0
 25 300
"""

def clock_face(num):
    return ((num % 30 )* 12)
      
    
user_input = int(input())
print(clock_face(user_input))