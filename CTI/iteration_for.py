#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 18:44:45 2021

@author: nat
"""

# Code of iteration lesson
# Please compare this with your code. Run this and mess with this code.
def main():
    # ============ Slide # 5: Sequences: elements:  =========
    print("\nSlide # 5: Sequences: elements:")
    a_sequence1 = [1, 2, 3, 4]
    a_sequence2 = "code"
    print('a_sequence1[1] = ', a_sequence1[1])
    print('a_sequence2[1] = ', a_sequence2[1])
    print('a_sequence1[-1] = ', a_sequence1[-1])
    print('a_sequence2[-1] = ', a_sequence2[-1])

    # ============ Slide # 7: Sequences: ranges:  =========
    print("\nSlide # 7: Sequences: ranges:")
    print('range(5) = ', range(5))
    print('range(5) as a list = ', list(range(5)))

    # ============ Slide # 8: Sequences: ranges:  =========
    print("\nSlide # 8: Sequences: ranges:")
    # print('range(2.5) = ', range(2.5)) # TypeError: 'float' object cannot be interpreted as an integer
    print('range(1, 6, 2) = ', list(range(1, 6, 2)))
    # print('range(1, 6, 0) = ', list(range(1, 6, 0))) # ValueError: range() arg 3 must not be zero

    # ============ Slide # 15: Sequences: ranges:  =========
    print("\nSlide # 15: Iteration: for loops:")

    # Problem:
    # Given a phrase, write a Python program
    # to print the phrase in reverse order in
    # a single line using a for loop. For
    # example, given the word, "code" your
    # program must print "edoc".
    # input = word
    # output: print reverse order eodc
    # need to access from right to left using - indexing
    # plan:
    # 1. input = word
    # 2. for indexes in range of indexes
    #       2.1 print word[indexes]

    # implementation
    word = "code"
    for indexes in range(-1, -len(word) - 1, -1):
        print(word[indexes], end="")


if __name__ == "__main__":
    main()
    
    
def printnums(x,y):
    for h in range(y):
        print("We made it here!")
        for i in range(x):
            print("We made it here!")

printnums(5, 3)