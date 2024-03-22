# Recursive implementation of n! (n-factorial) calculation
def factorial(n):
    # Base case: n = 0 or 1
    if n <= 1:
        return 1

    # Recursive case: n! = n * (n - 1)!
    return n * factorial(n - 1)

#big O(n) for time and space
"""
In total, nn calls are being made to the factorial function,
 making the time complexity O(n)O(n). Furthermore, the space complexity will also be in O(n)O(n). Recursion operates off of a stack, and because there are nn recursive calls, 
there will be nn stacks, which results in O(n)O(n) space


n = 5
res = 1
while n > 1:
    res = res * n
    n -= 1

"""