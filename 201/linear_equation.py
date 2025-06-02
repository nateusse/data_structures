#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 16:39:36 2021

Write a program that solves a linear equation ax = b in integers. 
Given two integers a and b (a may be zero), print a single integer 
root if it exists and print "no solution" or "many solutions" otherwise.
"""

a , b = int(input()), int(input())
if a == 0:
  if b == 0:
    print('many solutions')
  else:
    print('no solution')
elif b % a == 0:
  print(b // a)
else:
  print('no solution')