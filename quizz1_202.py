#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 16:29:23 2021

@author: nat
"""


print(-4**2 /4 +1) #-16/4 = /14+5  =1

print(6 < 5 and 1) # False and true is false

print(3 < 5 and 10 == 10) #True and True is true

print(2 + 10 and 4 == 2) # 12 and False is Flase

print(6 == 5 or 1+10)  # False or 11 is 11 ?(falso boolena y numero es numero)

print(1 + 5 + (5 == 5))  #   6 + (true) is 7? (adds 1 if true)




print(4 < 5 and 1) # true and 1 is 1 (numero y falso es numer)

print(4 < 5 and 1 == 1) # true and true is true

print(1 + 10 and 5 == 3)  # 11 and false is False (falso por 2 booleans())

print(5 == 5 or 1+10)  # true or 11 is True (boolean tru mas numero is true)

print(1 + 5 + (5 == 5)) # 6 and true is 7


# order of procedment 
#  (), **, %, -, ==, or
#  **, *, +, >=, not, and

def newtonSqrt(n, howmany):
   approx = 0.5 * n
   better = 0.5 * (approx + n/approx)
   while better != approx:
     approx = better
     better = 0.5 * (approx + n/approx)    
   return approx


print("Final value is: ", newtonSqrt(10, 20))


for numbers in range(4):
    print(numbers, end = ", ")
    
for letters in "Python":
    print(letters *2, end = "")


for numbers in range(8,0,-2):
    print(numbers, end = ", ")
    
code1 = "code"
for index in range(len(code1) -1, -1, -1):
    print(code1[index], end = ", ")   
    
for numbers in range(5):
    print(numbers, end = ", ")
    
for letters in "Python":
    print(letters, end = "")
print(" --------------")
    
    
s = "Accelerate!"
print(s[-2:len(s)])
print(s[-1])
print(s[len(s)-1])



str = "one two three four"
lst = str.split()
print(lst[1])


str = "CTI Accelerate"
a,b = str.split()
print(a,b)


str = "Racecar"
print(str[::-1])



strx = "CTI Accerlate"
stra = "CTI Accerlate"
strq = "CTI Accerlate"
for ch in strx: 
   print(strx)
   

for i in range(len(stra)-1):

       print(stra[i])

for i in range(len(strq)):
    print(strq[i])
