'''
Given three integers, in which two 
are equal to each other and the third 
one is different. Print the 
order number of this different one - 1, 2 or 3

'''

def find_index_diferent_nums_three_inputs(num1,num2,num3):
  result= set([num1,num2,num3])
  if len(result)==3:
    return 0
  else:
    return (4 - len(result))



user1,user2,user3 = int(input()),int(input()),int(input())
print(find_index_diferent_nums_three_inputs(user1,user2,user3))