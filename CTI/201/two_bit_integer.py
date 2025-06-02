#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 20:32:08 2022

@author: kali

Giving a 2 bit integer, print its left bit  (a 2's bit')
and then its right bit ( a ones bit). Use the operator of integer
division for obtaining the 2's bit and the
operator of taking remainder  for obaining the 
ones bit

Ej 0 >> 0 0
   1 >> 0 1
"""

# recibir un numero (max 3 para 1 1, min 0 pra 00)
#retornar 2 digits, binary
# procedimietno:division integer ( / uno) firsat digit
# segundo es el %
# convertir result into str
def two_bit_integer(num):
   
    first_bit = num % 2
    second_bit =  num // 2
    return(second_bit,first_bit  )

user_input = int(input())
print(two_bit_integer(user_input))