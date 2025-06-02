#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a string consisting of words separated by spaces. 
Determine how many words it has. To solve the problem, 
use the method count.

@author: nat
"""

word = input()
print( (word.count(" ", 0,-1)+1))
