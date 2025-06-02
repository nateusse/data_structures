'''
Given the two integers, print the least of them.
'''


def num_menor(num1, num2):
    res = [ str(num1) if num1<num2 else  str(num2)  ]
    return "".join(res)
user1, user2 = int(input()),int(input())
print(num_menor(user1, user2 ))

