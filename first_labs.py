#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a string that may contain a letter f.
 Print the index of the first and last occurrence of f.
 If the letter f occurs only once, then output its index once. 
 If the letter f does not occur, print -1.

@author: nat
"""

word = input()

if word.count("f")>=2:
    print(word.find("f"), word.rfind("f"))
elif word.find("f") == 0:
    print(-1)
else:
    print(word.find("f"))    