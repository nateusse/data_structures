'''
Given two non-zero integers,
 print "YES" if exactly one of them is 
 positive and print "NO" otherwise.

'''
#como chequeo que son 3
def positive_or_not(num1, num2):
    res = [ "YES" if (num1>0 and num2<0) or  (num1<0 and num2>0)  else "NO" ]
    return "".join(res)

user1, user2 = int(input()),int(input())
print(positive_or_not(user1, user2 ))