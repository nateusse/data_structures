#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 21:04:01 2022

@author: kali

Given the integer N - the number of seconds that is passed since midnight 
- how many full hours and full minutes are passed since midnight?

The program should print two numbers:
    the number of hours (between 0 and 23) 
    and the number of minutes (between 0 and 1339).

For example, if N = 3900, then 3900 seconds have passed since midnight - 
i.e. now it's 1:05am. So the program should print 1 65 - 1 
full hour is passed since midnight, 
65 full minutes passed since midnight.



"""


#Create def, return 2 values integers
# reveice one value
#procedimiento: if minutos mas de 1 hora, cont 1
#convertir a minutos  60 - 1 minuto
                    #  3900 es cuanto?    
# convertir a horas

def hours_and_minutes_after_midnight(seconds):  
    minutes = seconds // 60
    hours = minutes // 60
    return str(hours) + " " +str(minutes)
    

segundos = int(input())
print(hours_and_minutes_after_midnight(segundos))