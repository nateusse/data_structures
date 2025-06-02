#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 12:52:22 2021

@author: nat
"""


def missing(integers):
    n = len(integers)
    full_sum =n * (n +1)/2
    given_sum = 0
    for num in integers:
        given_sum = given_sum + num  
    return (full_sum - given_sum)


missing([0,1,2])