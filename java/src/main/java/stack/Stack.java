package stack;
import java.util.ArrayList;

/**
 * A simple stack implementation using an ArrayList.
 * Provides basic stack operations such as push, pop, and size.
 */
public class Stack {

    // Internal storage for the stack elements
    //ArrayList<Integer> stack = new ArrayList<Integer>();
    private ArrayList<Integer> stack;

    /**
     * Constructs an empty stack.
     */
    public Stack() {
        stack = new ArrayList<>();
    }

    /**
     * Pushes an element onto the stack.
     *
     * @param n the element to be pushed onto the stack
     */
    public void push(int n) {
        stack.add(n); // Add the element to the end of the list
    }

    /**
     * Pops the top element from the stack and removes it.
     *
     * @return the top element from the stack
     * @throws IllegalStateException if the stack is empty
     */
    public int pop() {
        if (stack.isEmpty()) {
            throw new IllegalStateException("Can't pop from empty stack.");
        }
        return stack.remove(stack.size() - 1); // Remove and return the last element
    }

    /**
     * Returns the current size of the stack.
     *
     * @return the number of elements in the stack
     */
    public int size() {
        return stack.size(); // Return the size of the list
    }

    /**
     * Checks if the stack is empty.
     *
     * @return true if the stack is empty, false otherwise
     */
    public boolean isEmpty() {
        return stack.isEmpty(); // Check if the list is empty
    }

    /**
     * Peeks at the top element of the stack without removing it.
     *
     * @return the top element of the stack
     * @throws IllegalStateException if the stack is empty
     */
    public int peek() {
        if (stack.isEmpty()) {
            throw new IllegalStateException("Cannot peek from an empty stack.");
        }
        return stack.get(stack.size() - 1); // Return the last element
    }

    /**
     * Prints the elements of the stack.
     */
    public void printStack() {
        System.out.println(stack); // Print the entire list
    }
}
