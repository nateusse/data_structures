#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a string, delete all its 
characters whose indices are divisible by 3.

@author: nat
"""


s = list(input())      
string = ""                           
del s[::3]                   
print(string.join(s))    