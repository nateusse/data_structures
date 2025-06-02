
'''
Given a three-digit integer X consisting of 
three different digits, print "YES" if its three 
digits are going in an ascending
 order from left to right and print "NO" otherwise.


MATCHING: if/else, comparisons, list comprehension

PLANNING:

for string: 
    receive num
    create list
    append to list num
    sort list
    compare list with num, if match "YES" else no

for integres:   
    recive string 3 digits
    get each num with modualr and diviisons oprateors
    compare first with second , c
'''



def ascending_three_digits(num):
    #LIST SORT 
    #lista = []
    #sorted = lista.sort() 
    #return ["YES" if sorted == num else "NO"]

    # nums
    uno, dos, tres = num//100, (num % 100)//10, num%10
    res = ["YES" if uno < dos and dos < tres else "NO"]
    return "".join(res)





user = int(input())
print(ascending_three_digits(user))