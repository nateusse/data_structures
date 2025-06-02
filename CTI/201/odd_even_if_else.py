'''
Given an integer, print "odd" if it is odd and print "even" otherwise.
'''


def odd_even(num):
    res = ["odd" if num % 2 != 0 else "even"]
    return "".join(res)
user = int(input())
print(odd_even(user))

# Other way with bitwise operator
res = (int(103) & 1) == 13
print(res) #even entonces ultimo bit es 0, sino seria 1