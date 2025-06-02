'''
Given three integers. 
Determine how many of them are equal to each other. 
The program must print one of the numbers: 
3 (if all are same),
 2 (if two of them are equal to each other 
 and the third one is different) 
or 0 (if all numbers are different).

'''

def equals_nums_three_inputs(num1,num2,num3):
  result= set([num1,num2,num3])
  if len(result)==3:
    return 0
  else:
    return (4 - len(result))





user1,user2,user3 = int(input()),int(input()),int(input())
print(equals_nums_three_inputs(user1,user2,user3))