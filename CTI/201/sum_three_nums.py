#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 20:07:07 2022

@author: kali

Write a program that takes three numbers and 
prints their sum. Every number is given on a
separate line. 
"""

#Plan
# recive 3 nums as integers
# return (function) sum

def sum_three_nums(num1, num2, num3):
       return num1 + num2 + num3
    

uno, dos, tres = int(input()), int(input()), int(input())
print(sum_three_nums(uno, dos, tres))