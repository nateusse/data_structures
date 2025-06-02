#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given three integers, print them in ascending order.


@author: nat
"""



"""
with sorting but dont do it like that
lista = []
a,b,c = input(),input(),input()
lista =[a,b,c]
lista.sort(reverse=False)
print(*lista, sep = "\n")
"""


a,b,c = int(input()),int(input()),int(input())
total = a+b+c
medio = total - min(a,b,c) - max(a,b,c)
print(min(a,b,c),medio, max(a,b,c),sep = "\n")

"""
a,b,c =input(),input(),input()
if a <= b <= c:
    print(a,b,c, end =" ")
elif a<=c<=b:
    print(a,c,b, end=" ")
elif b<=a<=c:
    print(b,a,c, end=" ")
elif b <= c <= a:
    print(b,c,a, end=" ")
elif c<=a<=b:
    print(c,a,b, end=" ")
print(c,b,a, end = " ")
"""