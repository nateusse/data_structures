"""
You are climbing a staircase. 
It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

"""

#recursivo que seria 0(n^2)
class Solution:
    def climbStairs(self, n: int) -> int:
        # Base case: n = 0 or 1
        if n <= 1:
            return 1

        # Recursive case: climbStairs(n) = climbStairs(n - 1) + climbStairs(n - 2)
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
    
#Dinamic programming 0(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        # Base case: n = 0 or 1
        if n <= 1:
            return 1

        # Initialize the number of ways to climb the first two steps
        one , two = 1, 1

        # Calculate the number of ways to climb the remaining steps
        for _ in range(n -1):
            temp = one
            one, two = one + two
            two = temp
        return one
    
