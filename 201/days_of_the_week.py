#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 17:39:51 2022

@author: kali


Days of week are numbered as: 0 — Sunday, 1 — Monday, 2 — Tuesday, ..., 6 — Saturday.
 An integer K in the range 1 to 365 is given. 
 Find and print the number of day of week for K-th day of year 
 provided that in this year January 1 was Thursday.  

Note: I will solve this problem following UMPIRE process at the end of this section.
"""

def days_of_the_week(num):
    return (int(num) + 3) % 7
      
    
user_input = input()
print(days_of_the_week(user_input))



