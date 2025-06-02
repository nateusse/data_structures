#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 13:11:11 2021

Given a three-digit integer X consisting of three different digits, print "YES" if its three digits are going in an ascending order from left to right and print "NO" otherwise.

@author: nat
"""

num = input()
print("YES" if num[0]<num[1]<num[2] else "NO")

print("YES") if all([num//100<(num//10)%10,(num//10)%10<num%10]) else print("NO")


