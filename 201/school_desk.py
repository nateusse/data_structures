#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 18:39:39 2022

@author: kali

A school decided to replace the desks in three classrooms. 
Each desk sits two students. 
Given the number of students in each class, 
print the smallest possible number of 
desks that can be purchased.

The program should read three integers: 
the number of students in each of the three classes,
a, b and c respectively.

For example, in the first test there are three groups.
The first group has 20 students and thus needs 10 desks. 
The second group has 21 students, 
so they can get by with no fewer than 11 desks. 
11 desks is also enough for the third group of 22 students. 
So we need 32 desks in total.

17 19 18 >> 28
25 21 23 >> 36
"""

def school_desk(room1, room2, room3):
   return (room1//2 + room2//2 + room3//2 + room1%2 + room2%2 + room3%2)
    
      
    
num1, num2, num3 = int(input()), int(input()), int(input())
print(school_desk(num1, num2, num3))

