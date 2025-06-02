#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a string that may contain a letter p. 
Print the index of the second occurrence of p. 
If the letter p occurs only once, then print -1, 
and if the string does not contain the letter p, 
then print -2.

@author: nat
"""

word = input()
if word.count("p") == 2:
  print(word.rfind("p"))
elif word.count("p") >= 2:
  print(word.find("p", word.find("p") + 1))
elif word.find("p") >= 1:
  print(-1)
else:
  print(-2)