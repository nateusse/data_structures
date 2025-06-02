"""
Let's call an integer a palindrome if it remains the same 
after reading its digits from right to left. 
Given a four-digit integer, print "YES" if it's a palindrome and print "NO" otherwise.
For example, the integer 1221 is a palindrome and we must print "YES", 
because it reads the same both from left to right and right to left.

Note: I will walk you over a complete UMPIRE process at the end of this section.

"""

# 1. Create function that receives input num four digits
#2 Compare first and last digit (Extracting them with //, and %)
#3 Compare second and third digit ((Extracting them with //, and %)
#4 Only if two comparison are equal, return string "YES"
#5 Otherwise, return string "NO"
def num_palindrome(num):
    res = ["YES" if num//1000==(num%10) and (num//10)%10==(num//100)%10 else "NO"]
    return "".join(res)
  
user = int(input())
print(num_palindrome(user))