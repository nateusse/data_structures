#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 17:29:09 2021

@author: nat
"""

h = (12345%10**4)//10**(4-1)
print(h)  #1000


j = 12345 % 2
print(j)  #t the last bit of any number %2

l = 101 >> 1
print(l)


z =  123 // 10
print(z)



num = 12345
i = 1

while( i <= len(str(num))):
    print( (num % 10**i)//10**(i-1) ,end="") 
    i = i+1