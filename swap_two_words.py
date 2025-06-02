#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a string consisting of exactly two words 
separated by a space. Print a new string with 
the first and second words swapped: the second
 word is printed first. 
 Consider all adjacent non-space characters a single word.

Can you solve it without using if-else and loops?

@author: nat
"""

word = input()
word1, word2 = word.split(" ")
print(word2,word1)
