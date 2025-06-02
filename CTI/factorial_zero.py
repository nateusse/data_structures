#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 09:11:42 2021


Given an integer n, return the number of trailing zeroes in n!.


@author: nat
"""


def trailingZero(n):
    quotient = n
    numOfZ = 0
    while 1:
        quotient = quotient // 5 ;
        numOfZ = numOfZ + quotient;
        if (quotient < 5):
            break;
    return numOfZ
        