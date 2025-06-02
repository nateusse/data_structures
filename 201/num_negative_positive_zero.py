
'''
For a given integer, a_number, print 1 if it is positive, 
-1 if it is negative, 
or 0 if it is equal to zero.
'''


def negative_positive_zero(num):
    res = ["-1" if num < 0 else "1" if num > 0 else "0" if num == 0 else ""]
    return "".join(res)

user = int(input())
print(negative_positive_zero(user))