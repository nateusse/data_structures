













#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a string of four numbers,
 print "Even" if the summation of all
 of the numbers is even, and "Odd" if the
 summation is odd.

@author: nat

print("Even" if total%2==0 else "Odd" )

"""



def sum_odd_or_even(num):
    nums_list = num.split()
    resu = ["Even" if (sum(int(i) for i in nums_list))%2==0 else "Odd"]
    return "".join(resu)

num = input()       
print( sum_odd_or_even(num))