#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a sequence of non-negative integers, 
where each number is written (input) in a separate line.
The sequence ends with 0. Print the maximum of the sequence.

@author: nat
"""

s, lista = int(input()) , []
while s != 0:
  lista.append(s)
  s = int(input())
print(max(lista))

