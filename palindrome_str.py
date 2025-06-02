#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Determine if a string entered by the user 
is a palindrome or not. A palindrome 
is a string that is the same from left to 
right and right to left. Assume all entries are lowercase. 

@author: nat
"""

s = input()
print(s.find(s[::-1])!= -1) 
        
#UNDESTAND-----------------------------------------------
      # Input User / output Boolean if palindrome or not
      # Questions: Spaces, uppercase
      
      
      
#MATCH -------------------------------------------------- 
        # Reverse slicing / Find function / comparison operator
        
        
#PLAN --------------------------------------------------
         #1. Receive input
         #2. Use function find in string:
             #2.1 Find in reverse, if string !=-1 is true
             

#IMPLEMENT ---------------------------------------------
       # s = input()
       #print(s.find(s[::-1] != -1) 
        


#REVIEW --------------------------------------
           #Input "maam" --------> Expected output True 
           #m[-1]  m[1]
           #a[-2]  m[2]
           #a[-3]  m[3]
           #m[-4]  m[4]
          
#EVALUATE ---------------------------------------
  #Potencial: 0(1) I think? Not sure becuase only happen once but goes throw the entire string
  # Weakness: Not sure if I can use built in functions