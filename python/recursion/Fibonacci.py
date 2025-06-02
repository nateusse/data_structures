class Fibonacci:
    """
    #RECURSIVE
    def fibonacci_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0  # Base case: Fibonacci(0) = 0
    if n == 1:
        return 1  # Base case: Fibonacci(1) = 1
    # Recursive calculation
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    """

    """
    #ITERATIVE
    def fibonacci_iterative(n: int) -> int:
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers")
        if n == 0:
            return 0  # Base case: Fibonacci(0) = 0
        if n == 1:
            return 1  # Base case: Fibonacci(1) = 1
        # Initialize the first two Fibonacci numbers
        previus, current = 0, 1
        # Calculate the nth Fibonacci number
        for _ in range(2, n + 1):
              previus, current = current, previus + current  # Update the values
        return current # Return the nth Fibonacci number
        
        
        #time complexity: O(n), space complexity: O(1)
        """

    #MEMOIZATION
    @staticmethod   #no need to create an instance of the class, no states
    def fibonacci_memoization(n: int, memo: dict = {}) -> int:
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers")
        if n == 0:
            return 0  # Base case: Fibonacci(0) = 0
        if n == 1:
            return 1  # Base case: Fibonacci(1) = 1
        if n not in memo:
            # Recursive calculation
            memo[n] = Fibonacci.fibonacci_memoization(n - 1, memo) + Fibonacci.fibonacci_memoization(n - 2, memo)
        return memo[n]
    
    #time complexity: O(n), space complexity: O(n)
    #@STATICMETHOD: no need to create an instance of the class no states (self)
    # No need for fb=Fibonacci print(fb. fibonacci_memoization(5)), I can print(Fibonacci.fibonacci_memoization(5))
   