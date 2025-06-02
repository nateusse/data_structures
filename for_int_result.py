#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 18:48:28 2021


Given two integers A and B (A ≤ B). 
Print all numbers from A to B inclusively.


@author: nat
"""

a,b = int(input()), int(input())
for i in range(a,b+1): print(i, end=" ")