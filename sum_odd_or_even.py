#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a string of four numbers,
 print "Even" if the summation of all
 of the numbers is even, and "Odd" if the
 summation is odd.

@author: nat

print("Even" if total%2==0 else "Odd" )

"""

num = input()
test_list = num.split()
count = 0
  
for i in test_list:
    for i in str(i):
           count += int(i)
       
print("Even" if count%2==0 else "Odd" )