#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a list of integers with duplicates, 
write a Python function to return a new 
list of numbers with duplicates removed. 
For example, given the lists [1, 2, 3, 2, 2, 1, 1, 3, 3 ] 
return [1, 2, 3]. In mathematics a set is a 
collection of unique set of elements. 
So this is a classic set creation operation. 
However, since we are not yet there on Python sets, 
you are not allowed to use any set or dictionary 
operations here. Also, investigate how you can 
solve this using list comprehension.

@author: nat
"""

def remove_duplicates(a_list):
    distinct_elements = []
    [distinct_elements.append(i) for i in a_list  if i not in distinct_elements]    
    return (distinct_elements)


