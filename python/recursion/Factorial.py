class Factorial:

    def factorial(self, n: int) -> int:  
        if n < 0: raise ValueError("Factorial is not defined for negative numbers")
        if n == 1 or n == 0: return 1
        
        # Recursive implementation of n! (n-factorial) calculation
        return n * self.factorial(n - 1)
    
    #Time O(n), Space O(n)
    
"""
for i in range(2, n + 1):  #from 2 to n inclusive
        result *= i
    return result
time: O(n),  espacio: O(1)


#MEMOIZACION
if n in memo:  # If calculated, return value
        return memo[n]

memo[n] = n * factorial_memoization(n - 1, memo)
    return memo[n]

time: O(n),  espacio: O(n)
"""