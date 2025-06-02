#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 19:58:49 2021

@author: nat
"""

name = input()
last_char_name = name[-1]
value_ascii = int(ord(last_char_name))
value1 = value_ascii%10
value2 = (value_ascii%100)//10
bin_value1 = (bin(value1))
bin_value2 = (bin(value2))
if bin_value1[-1] == bin_value2[-1]:
    print ("Lsb matches: "  + str(bin_value1[-1]) + " " +str(bin_value2[-1]))
else:  print ("Lsb does not match: "  + str(bin_value2[-1]) + " " +str(bin_value1[-1]))
