'''
Given an integer, print "YES" if it
 is a three-digit number and print "NO" otherwise.

'''
#como chequeo que son 3
def three_digit_num(num):
    res = ["NO" if num//100 == 0 or (num// 100)>9 else "YES"]
    return "".join(res)

user = int(input())
print(three_digit_num(user))

