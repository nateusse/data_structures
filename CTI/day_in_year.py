#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Given a month - an integer from 1 to 12, print the number of days in it in the year 2017.

@author: nat
"""

month = int(input())
if (month == 12 or month == 10 or month == 8 or month == 7 or month == 5 or month == 3 or month == 1):
    print(31)
elif (month==2):
    print(28)
else:
    print(30)