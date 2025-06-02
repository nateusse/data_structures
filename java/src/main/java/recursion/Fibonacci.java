package recursion;

import java.util.HashMap;

public class Fibonacci {

    /**
     * Recursive implementation of Fibonacci.
     *
     * @param n The index of the Fibonacci sequence to calculate.
     * @return The nth Fibonacci number.
     * @throws IllegalArgumentException If n is negative.
     */

    /* 
    public static int fibonacciRecursive(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("Fibonacci is not defined for negative numbers");
        }
        if (n == 0) {
            return 0; // Base case: Fibonacci(0) = 0
        }
        if (n == 1) {
            return 1; // Base case: Fibonacci(1) = 1
        }
        // Recursive calculation
        return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
    }
    */

    //FOR, iterative

    /**
     * Iterative implementation of Fibonacci.
     *
     * @param n The index of the Fibonacci sequence to calculate.
     * @return The nth Fibonacci number.
     * @throws IllegalArgumentException If n is negative.
     */
    /* 
    public static int fibonacciIterative(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("Fibonacci is not defined for negative numbers");
        }
        if (n == 0) {
            return 0; // Base case: Fibonacci(0) = 0
        }
        if (n == 1) {
            return 1; // Base case: Fibonacci(1) = 1
        }

        // Initialize the first two Fibonacci numbers
        int previous = 0, current = 1;

        // Calculate the nth Fibonacci number
        for (int i = 2; i <= n; i++) {
            int next = previous + current; // Next Fibonacci number
            previous = current;            // Update previous
            current = next;                // Update current
        }

        return current;
    }
        */

        /**
     * Memoized implementation of Fibonacci using a HashMap.
     *
     * @param n The index of the Fibonacci sequence to calculate.
     * @param memo A HashMap to store previously calculated Fibonacci numbers.
     * @return The nth Fibonacci number.
     * @throws IllegalArgumentException If n is negative.
     */
    public static int fibonacciMemoized(int n, HashMap<Integer, Integer> memo) {
        if (n < 0) {
            throw new IllegalArgumentException("Fibonacci is not defined for negative numbers");
        }
        if (n == 0) {
            return 0; // Base case: Fibonacci(0) = 0
        }
        if (n == 1) {
            return 1; // Base case: Fibonacci(1) = 1
        }

        if (!memo.containsKey(n)) {
            // Recursive calculation with memoization
            memo.put(n, fibonacciMemoized(n - 1, memo) + fibonacciMemoized(n - 2, memo));
        }

        return memo.get(n);
    }



}
