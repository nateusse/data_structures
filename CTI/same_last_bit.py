
"""
@author: nat


Given two input numbers, 
print 'True' if the last least significant bit 
of the two number match and 'False' if they don't.


"""

input_user = input()
list_user = input_user.split()
a=  bin(int(list_user[0]))
b= bin(int(list_user[1]))
if a[-1]==b[-1]:
  print(True)
else:
    print(False)