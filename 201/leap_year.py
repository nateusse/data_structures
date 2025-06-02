#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given the year number. You need to check if this year is a leap year. If it is, print LEAP, otherwise print COMMON.

The rules in the Gregorian calendar are as follows:

a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
a year is always a leap year if its number is exactly divisible by 400
Warning. The words LEAP and COMMON should be printed all caps.

@author: nat
"""

year = int(input())
print("LEAP" if year%400 == 0  or (year%4 == 0 and year%100 != 0)  else "COMMON")