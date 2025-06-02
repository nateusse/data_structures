#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: nat



In the first line, print the third character of this string.
In the second line, print the second to last character of this string.
In the third line, print the first five characters of this string.
In the fourth line, print all but the last two characters of this string.
In the fifth line, print all the characters of this string with even indices (remember indexing starts at 0, so the characters are displayed starting with the first).
In the sixth line, print all the characters of this string with odd indices (i.e. starting with the second character in the string).
In the seventh line, print all the characters of the string in reverse order.
In the eighth line, print every second character of the string in reverse order, starting from the last one.

In the ninth line, print the length of the given string.

"""

st =  input()
print(st[2]) #first
print(st[-2])  #second
print(st[:5])   #third
print(st[:-2])   #fourt
print(st[0::2])  # cinco
print(st[1::2])  #six 
print(st[-1::-1]) #siete
print (st[-1::-2] ) #ocho
print(len(st))