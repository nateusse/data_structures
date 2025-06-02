"""
Given three integers, print the least of them.


MATCHING: if/else, comparisons, list comprehension


Input: nums (integer)
output: num

PLAN:
 
recieve num
create while loop to reverse num:
    1. Create while loop condition num differnt from 0
    2. Extract with modular 10 (each alst digit)
    
"""



def smallest_num(num1,num2,num3):
   
    res = [str(num1) if (num1 <= num2) and (num2 <= num3) else str(num2) if (num2 <= num1) and (num2 <= num3) else str(num3)]
    return "".join(res)





user1,user2,user3 = int(input()),int(input()),int(input())
print(smallest_num(user1,user2,user3))