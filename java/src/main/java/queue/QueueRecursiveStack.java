package queue;
import java.util.Stack;

public class QueueRecursiveStack<T> {
    private Stack<T> stack;
    
    public QueueRecursiveStack() {
        stack = new Stack<>();
    }
    
    // Add element to queue
    public void enqueue(T item) {
        stack.push(item);
    }
    
    // Remove element from queue
    public T dequeue() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty");
        }
        
        if (stack.size() == 1) {
            return stack.pop();
        }
        
        // Remove top element
        T item = stack.pop();
        // Recursively remove all other elements
        T result = dequeue();
        // Push back the removed element
        stack.push(item);
        
        return result;
    }
    
    // Get front element
    public T peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty");
        }
        
        if (stack.size() == 1) {
            return stack.peek();
        }
        
        T item = stack.pop();
        T result = peek();
        stack.push(item);
        
        return result;
    }
    
    public boolean isEmpty() {
        return stack.isEmpty();
    }
    
    public int size() {
        return stack.size();
    }
}
