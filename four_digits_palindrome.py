"""
Let's call an integer a palindrome 
if it remains the same after reading 
its digits from right to left. Given a four-digit integer, 
print "YES" if it's a palindrome and 
print "NO" otherwise.


MATCHING: if/else, comparisons, list comprehension, palindrome


Input: num (integer)
output: String, "YES" or "NO"

PLAN:

for num as string: 
    receive num
    create list
    append to list num
    sort list
    compare list with num, if match "YES" else no

for integres:   
    recive num
    create while loop to reverse num:
        1. Create while loop condition num differnt from 0
        2. Extract with modular 10 (each alst digit)
    
"""



def four_digits_palindrome(num):
    #LIST SORT 
    #return ["YES" if num[::-1] == num else "NO"]

    # nums
    inputUser = num
    reversed_num = 0  
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    res = ["NO" if reversed_num != inputUser else "YES"]
    return "".join(res)





user = int(input())
print(four_digits_palindrome(user))