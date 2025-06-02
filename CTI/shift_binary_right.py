
"""
Given two input numbers, print out the two 
numbers with their binary value shifted to the right by 1 bit.
@author: nat
"""

user_input = input()
list_input = user_input.split()
value1 = int(list_input[0])
value2 = int(list_input[-1])

bin_value1 = value1 >> 1
bin_value2 = value2 >> 1
print(str(bin_value1),str(bin_value2))
