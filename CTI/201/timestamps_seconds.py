#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 21:15:41 2022

@author: kali

Given two timestamps of the same day: 
    a number of hours, 
    minutes 
    and seconds for both of the timestamps. 
    The moment of the first timestamp happened 
    before the moment of the second one. 
    Calculate how many seconds passed between them.
"""


#time stamps 
# iput numbers hours, mminutes, seconds X2
#return seconds 1 unit integer
# rpcedmiento:
    
    #convertir horas a minutos, minutos  a segundos
    # suamr total
    #mismo procedimeitno otra estampa
    #restar
    #return resta

def stamps_seconds(hours1, minutes1, segundos1,hours2, minutes2, segundos2):  
    hours1_to_minutes = hours1 * (60**2)
    minutes1_to_seconds = minutes1 * 60
    total_stamp1 = segundos1 + minutes1_to_seconds + hours1_to_minutes
    #second stamp
    hours2_to_minutes = hours2 * (60**2)
    minutes2_to_seconds = minutes2 * 60
    total_stamp2 = segundos2 + minutes2_to_seconds + hours2_to_minutes
    result_seconds = total_stamp2 - total_stamp1
    return str(result_seconds)
    

hours1, minutes1, segundos1 = int(input()),int(input()),int(input())
hours2, minutes2, segundos2 = int(input()),int(input()),int(input())
print(stamps_seconds(hours1, minutes1, segundos1,hours2, minutes2, segundos2))