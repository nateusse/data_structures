#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a string in which the letter h occurs at least twice. 
Remove from that string the first and the last occurrence 
of the letter h, as well as all the characters between them.


@author: nat
"""

word = input()
print(word[:word.index("h")] + word[word.rindex("h") + 1:])