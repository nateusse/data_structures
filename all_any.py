#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 12:08:55 2021

@author: nat
"""

#all() returns True if all elements in the given iterable are true
numbers1=[1,2,3,0] #0 is false
print(all(numbers1))
# #any() returns True if any element of an iterable is True
numbers2=[1,2,3,0]
print(any(numbers2))
# # challenge 1
my_list = [1, 2, 3, 4]
print(any(my_list))
# # challenge 2
my_list = [0, False]
print(all(my_list))
# print(any(my_list))
# # challenge 3 
my_list = [1, 3, 4, 0]
print(all(my_list))
# # challenge 4
my_list = [0, False, 5]
print(all(my_list))  
print(any(my_list))  
# # challenge 5
my_list = []
print(all(my_list))  #true
print(any(my_list))  #false
 
# # challenge 6
my_string = "I'm awesome!"
print(all(my_string))  #true
print(any(my_string))   #true
# # challenge 7
my_string = '012'
print(all(my_string))  #true
print(any(my_string))   # true
# # challenge 8
my_string = ''
print(all(my_string))    #true
print(any(my_string))   #false