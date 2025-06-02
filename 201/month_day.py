#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 16:24:33 2021

Given a month (an integer from 1 to 12) and a day in it (an integer from 1 to 31) 
in the year 2017, print the month and the day of the next day to it.


MATCHING: conditionals, 


PLANNING:
"""


month, day = int(input()), int(input())

if month in (1, 3, 5, 7, 8, 10, 12): month_length = 31
elif month == 2:month_length = 28
else: month_length = 30



if day < month_length: day += 1
else:
    day = 1
    if month == 12:
        month = 1
    else:
        month += 1
print(month)
print(day)