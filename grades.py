#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 19:56:17 2021

@author: nat
"""

total = 80
grade = ""
if total >= 90:
    grade = "A"
elif total >= 80:
    grade = "B"
elif total >= 70:
     grade = "C"
elif total >= 60:
     grade = "D"
else:
    grade = "F"
    
print(grade)