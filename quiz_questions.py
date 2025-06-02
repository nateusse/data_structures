#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 20:31:32 2021

@author: nat

user_input = input().split() 
print(int(user_input[0]) + int(user_input[-1]))


a = 2 
b = 4 
c = 8
print(a, b, c, sep="*") 


print(4 >> 1)

if False: 
    print("one", end=" ")
    if True:
        print("two",end=" ")
    else: 
        print("three", end=" ")
else:
    print("three", end=" ")
print("four", end =" ")


print(True and False and True or False)


"""

user_input = "1 2 3 4 5".split() 
user_input = user_input[::-1] 
print(int(user_input[0]) + int(user_input[-2]))

a = 2 
b = 4 
c = 8
print(a, b, c, sep ="") 

print(True or False and True or False)



print(4 << 1)
print((78910%10**100)//10**(100-1))


if False: 
    print("one", end=" ")
    if True:
        print("two",end=" ")
    else: 
        print("three", end=" ")
else:
    print("three", end=" ")
print("four", end =" ")