#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a string, cut it into two equal parts. 
If the length of the string is odd, 
leave the middle character within the first chunk, 
so that the first string contains one more character 
than the second. Now print a new string on a single 
row with the first and second halves swapped: 
second half first and the first half last.

Can you solve it without using if?

@author: nat


"""

string = input()
firstpart = string[:int(len(string)/2)]
secondpart = string[int(len(string)/2):]
result = secondpart+firstpart
print (result)