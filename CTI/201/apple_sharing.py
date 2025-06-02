#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 20:51:05 2022

@author: kali

N students take K apples and distribute them among each other evenly. 
The remaining (the indivisible) part remains in the basket. 
How many apples will each single student get? 
How many apples will remainin the basket?

The program reads the numbers N and K. 
It should print the two answers for the questions above.
"""


#create function
# receive amount of students (int)
# recive numbers apples (int)

#return apples per studen disible
# get how many apples stay in the absquet reminder
def apple_sharing(students, apples):  
    apples_per_student = apples//students
    reminder_apples = apples % students
    return (str(apples_per_student) + "\n" + str(reminder_apples))
    

students_amount, apples_amount = int(input()), int(input())
print(apple_sharing(students_amount, apples_amount))