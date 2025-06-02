#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 23:14:13 2021

@author: nat
"""

a_list = [1,2,[3,4],"Code"]
for indexes in range(-1,-len(a_list)-1,-1):
    print(a_list[indexes],end=", ")
#Code, [3,4],2,1