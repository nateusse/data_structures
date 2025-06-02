#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 20:32:12 2021

@author: nat



Let's call an integer a palindrome if it remains the same after reading its digits from right to left. Given a four-digit integer, print "YES" if it's a palindrome and print "NO" otherwise.

For example, the integer 1221 is a palindrome and we must print "YES", because it reads the same both from left to right and right to left.

"""

num = input()
print( "YES" if (num[0]==num[3] and num[1]==num[2] ) else "NO")


num = int(input())
if (num % 100) // 10 == (num % 1000) // 100 and (num % 10) == (num //1000):
    print ("YES")
print ("NO")




