package recursion;
import java.util.HashMap;


public class Factorial {


    /**
     * Recursive implementation of factorial.
     * 
     * @param n The number to calculate factorial for.
     * @return The factorial of n.
     * @throws IllegalArgumentException If n is negative.
     */
    /* 
    public int factorialRecursive(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("Factorial is not defined for negative numbers");
        }
        if (n == 0 || n == 1) {
            return 1; // Base case: 0! = 1, 1! = 1
        }
        // Recursive calculation of n!
        return n * factorialRecursive(n - 1);
    }

   */
    /**
     * Iterative implementation of factorial.
     * 
     * @param n The number to calculate factorial for.
     * @return The factorial of n.
     * @throws IllegalArgumentException If n is negative.
     */
    /* 
    public int factorialIterative(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("Factorial is not defined for negative numbers");
        }
        int result = 1;
        for (int i = 2; i <= n; i++) { // Loop from 2 to n
            result *= i;
        }
        return result;
    }
    */
    /**
     * Memoized implementation of factorial using a HashMap.
     */
    private final HashMap<Integer, Integer> memo = new HashMap<>();

    /**
     * Memoized recursive implementation of factorial.
     * 
     * @param n The number to calculate factorial for.
     * @return The factorial of n.
     * @throws IllegalArgumentException If n is negative.
     */
    public int factorialMemoized(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("Factorial is not defined for negative numbers");
        }
        if (n == 0 || n == 1) {
            return 1; // Base case
        }
        if (memo.containsKey(n)) { // If already calculated, return from memo
            return memo.get(n);
        }
        // Compute factorial, store in memo, and return the result
        int result = n * factorialMemoized(n - 1);
        memo.put(n, result);
        return result;
    }


}
    
