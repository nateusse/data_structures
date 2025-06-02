#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 12:51:23 2021

@author: nat

"""
 
def oddOcurrence(nums):
   total = 0
   for element in nums:
       total = total ^ element

   return total



print(oddOcurrence([-9, -12, 4, 8, -12,4,2,-12, -9,2,12, 7,8, 7, 12]))