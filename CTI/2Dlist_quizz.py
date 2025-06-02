#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 13:45:56 2021

@author: nat
"""

"""
Select the valid ways to initialize a 5X5 2D list, 
and fill it with 0's. 

rows, cols = (5, 5)

arrs = [[0]*cols]*rows
print(arrs)

rows, cols = (5, 5)
arrs=[]
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(0)
    arrs.append(col)
    
print(arrs)


rows, cols = (5, 5)
args = [[0 for i in range(cols)] for j in range(rows)]
print(args)




my_lst = [["A","B","C"],[1,2,3]]
my_lst[2] = ['*','&','$']

my_lst.append( '*','&','$')

my_lst.append( ['*','&','$']) #correcto


my_lst = [["A","B","C"],[1,2,3]]

my_lst[0].append("D")
print(my_lst)


my_lst = [["A","B","C","D"],[1,2,3]]

print(my_lst[len(my_lst) -1 ])


"""

