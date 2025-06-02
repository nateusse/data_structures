#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Sep 20 19:12:42 2022

@author: kali

Given a year (as a positive integer), 
find the respective number of the century. 
Note that, for example, 20th century began with the year 1901.

1401	15
1400	14
1389	14
785	     8
2017	21
2001	21
2000	20
1999	20
1950	20

"""


def century(year):
       return (year - 1) // 100 + 1

user_input= int(input())
print(century(user_input))
