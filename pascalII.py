#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a list of positive integers called integers, 
print a row with len(integers)+1 entries as follows:

first and the last number printed will be 1
The ith number will be the sum of the value of the (ith-1)
 and ith numbers in the list integers
output a list

 
@author: nat


lst, result = [int(i) for i in input().split()], []
result = [lst[i] + lst[i + 1] for i in range(len(lst)-1)]
print ("1", *result, end = " " + "1")



def pascal(lst):
    result = []
    for i in range(len(lst)):
        c = 1;
        for j in range(1, i + 1):
            print(c, end = " ");
            c = int(c * (i - j) / j);
        print("");

            
    return result
    

print(pascal("1 5 10 5 1"))



begin = i
        end = len(lst)-1
        result.append(sum(int(lst[begin:end])) )
"""

def pascal(lst):
    result = []
    for i in range(len(lst)):
           total = 0
           total = [lst[i] + lst[i + 1] for i in range(len(lst)-1)]
           result = [1,*total,1]
    return result
print(pascal([1,3,3,1]))

