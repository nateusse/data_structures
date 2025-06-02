#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
There was a set of cards with numbers from 1 to N. 
One of the cards is now lost. Determine the number 
on that lost card given the numbers for the remaining
 cards.

Given a number N, followed by N − 1 integers 
representing the numbers on the remaining cards 
(distinct integers in the range from 1 to N). 
Find and print the number on the lost card.

@author: nat


"""


n=int(input())   
total, missing =0,0  
for i in range(n+1):
  total += i
for i in range (n-1):
    nums = int(input())
    missing += nums
res = total - missing
print(res)





