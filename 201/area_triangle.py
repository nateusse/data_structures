#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 20:11:56 2022

@author: kali

Write a program that reads the length of the 
base and the height of a right-angled triangle 
and prints the area. Every number is given on a
 separate line.
"""

# receive 2 nums as in (b and h)
# create functionreturn area
# foruma area (1/2)bh
# preguntas: Cuantos decimales? Con decimales?
# Ojo con parentesis en la formula

def area_triangulo(base,altura):
       return (((1/2)*base)*altura)
    

uno, dos = int(input()), int(input())
print(area_triangulo(uno, dos))