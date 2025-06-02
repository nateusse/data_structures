#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 20:19:44 2022

@author: kali


Write a program that greets the user by printing 
the word "Hello", a comma, the name of the user
 and an exclamation mark after it.
 See the examples below.

Warning. Your program's output should strictly 
match the desired one, character by character. 
There shouldn't be any space between the name 
and the exclamation mark. You can use + operator 
to concatenate two strings. See the lesson for details.
"""


#recibir input string
#return "Hello", a comma, the name of the user and an exclamation mark after it.
# 
def hello_harry(name):  
    return "Hello, " + name +  "!" 
    
    

user_input = input()
print(hello_harry(user_input))