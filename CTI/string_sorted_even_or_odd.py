#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a string of four numbers,
 if the numbers are in ascending order,
 print "Sorted & even" if the summation of all of the numbers is even, 
 and "Sorted & odd" if the summation is odd. If the numbers are not sorted, 
 and the summation of all of the numbers is even, print "Unsorted & even', 
 and "Unsorted & odd" if the summation of all of the numbers is odd.
 
 
@author: nat
"""
"""
num = input()
nums = num.split()
count = 0

for i in nums :
    for i in str(i):
            count += int(i)
if (count%2==0 and nums[0]<nums[1]<nums[2]<nums[3]):
                print ("Sorted & even")  
if (count%2==0 and not nums[0]<nums[1]<nums[2]<nums[3]):
                print ("Unsorted & even")
elif(count%2!=0 and nums[0]<nums[1]<nums[2]<nums[3]):
                 print ("Sorted & odd")  
else:
    print ("Unsorted & odd")
    
    """
    
user_input = input().split()
int_input = []
summation = 0
isSorted = ""
isEven = ""

# convert input to ints
for num in user_input:
    new_num = int(num)
    int_input.append(new_num)
    # find summation
    summation = summation + new_num
    
# check if it is sorted
if int_input[0] <= int_input[1] <= int_input[2] <= int_input[3] :
    isSorted = "Sorted"
else:
    isSorted = "Unsorted"
    
# check for even/odd
if summation % 2 == 0:
    isEven = "even"
else:
    isEven = "odd"

#print result  
print(isSorted, " & ", isEven, sep="")