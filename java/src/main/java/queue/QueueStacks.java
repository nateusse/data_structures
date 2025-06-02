package queue;
import java.util.Stack;

/**
 * Implementation of a Queue using two stacks.
 */
public class QueueStacks<T> {
    private Stack<T> inputStack;  // stack elments are pushed to
    private Stack<T> outputStack; // Stack for dequeue FIFO

    /**
     * Constructor to initialize the two stacks.
     */
    public QueueStacks() {
        inputStack = new Stack<>();
        outputStack = new Stack<>();
    }

    /**
     * Add an element to the rear of the queue.
     * @param value The value to be added.
     */
    public void enqueue(T value) {
        inputStack.push(value); // Push the value onto the input stack
    }

    /**
     * Remove and return the front element of the queue.
     * @return The front element, or null if the queue is empty.
     */
    public T dequeue() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty");
        }

        // Transfer elements from inputStack to outputStack if outputStack is empty
        if (outputStack.isEmpty()) {
            transferElements();
            /*while (!stack1.isEmpty()) {
                stack2.push(stack1.pop());
            } */
        }

        return outputStack.pop(); // Pop the front element from outputStack
    }

    /**
     * Get the front element of the queue without removing it.
     * @return The front element, or null if the queue is empty.
     */
    public T peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty");
        }

        // Transfer elements from inputStack to outputStack if outputStack is empty
        if (outputStack.isEmpty()) {
            transferElements();
        }

        return outputStack.peek(); // Peek the front element from outputStack
    }

    /**
     * Check if the queue is empty.
     * @return True if the queue is empty, false otherwise.
     */
    public boolean isEmpty() {
        return inputStack.isEmpty() && outputStack.isEmpty();
    }

    /**
     * Get the size of the queue.
     * @return The number of elements in the queue.
     */
    public int size() {
        return inputStack.size() + outputStack.size();
    }

    /**
     * Transfer all elements from inputStack to outputStack.
     */
    private void transferElements() {
        while (!inputStack.isEmpty()) {
            outputStack.push(inputStack.pop());
        }
    }

    
}
