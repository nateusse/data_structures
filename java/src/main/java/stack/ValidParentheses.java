package stack;

import java.util.HashMap;
import java.util.Stack;

/*
*  You are given a string s consisting of the following characters:
* '(', ')', '{', '}', '[' and ']'.
* The input string s is valid if and only if:
*  Every open bracket is closed by the same type of close bracket.
* Open brackets are closed in the correct order.
* Every close bracket has a corresponding open bracket of the same type.
* Return true if s is a valid string, and false otherwise.
*
* */
public class ValidParentheses {

        /**
         * Determines if a string containing parentheses is valid.
         * A string is valid if:
         * - Every open bracket is closed by the same type of close bracket.
         * - Open brackets are closed in the correct order.
         * @param s The input string containing '(', ')', '{', '}', '[' and ']'.
         * @return true if the string is valid, false otherwise.
         */
        public boolean isValid(String s) {
            // Map to match closing brackets to their corresponding opening brackets
            HashMap<Character, Character> map= new HashMap<>();
            map.put(')', '(');
            map.put(']', '[');
            map.put('}', '{');

            // Stack to track opening brackets
            Stack<Character> stack = new Stack<>();

            // Iterate through each character in the string
            for (char c : s.toCharArray()) {
                if (map.containsKey(c)) { // If it's a closing bracket
                    // Check if the stack is not empty and the top element matches
                    if (!stack.isEmpty() && stack.peek() == map.get(c)) {
                        stack.pop(); // Remove the matching opening bracket
                    } else {
                        return false; // Invalid case: no match or stack is empty
                    }
                } else { // It's an opening bracket
                    stack.push(c); // Add it to the stack
                }
            }

            // If the stack is empty, all brackets were matched correctly
            return stack.isEmpty();
        }



}
