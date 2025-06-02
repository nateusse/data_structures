"""
Given an integer n,
 return the number of trailing 
 zeroes in n!.

Ej: 3! -> 0
    5! -> 1 (120 tiene un cero)


Receive a single num in the function
Have a counter starting whith zero to count total zeros
Knowing from previus videos that it carries zeros bases on 5 create while and:
    - divide num by 5 and add amount of zeros to counter
    - increase power (avoid infinitive loop, break while) to division equals zero

"""


def factorials(n):
    zero, power = 0, 5
    while (n // power) != 0:
        zero += n // power
        power *= 5
    return zero

user = int(input())
print(factorials(user))