package queue;
/**
 * A simple implementation of a Queue using a linked list.
 */
public class QueueLinkedList<T> {

    /**
     * Inner class representing a node in the linked list.
     */
    private static class Node<T> {
        private T data; // The value stored in the node
        private Node<T> next; // Pointer to the next node

        public Node(T data) {
            this.data = data;
            this.next = null;
        }
    }
    private Node<T> front; // Points to the front of the queue
    private Node<T> rear;  // Points to the rear of the queue
    private int size;      // Tracks the size of the queue

    /**
     * Constructor to initialize an empty queue.
     */
    public QueueLinkedList() {
        front = null;
        rear = null;
        size = 0;
    }

     /**
     * Add an element to the rear of the queue.
     * @param value The value to be added.
     */
    public void enqueue(T value) {
        Node<T> newNode = new Node<>(value);
        if (isEmpty()) { //if rear = null, if queue is empty
            f front = rear = newNode;
        } else {
            rear.next = newNode; // Link the new node at the rear
            rear = newNode;      // Update the rear pointer
        }
        size++;
    }
    
    /**
     * Remove and return the element from the front of the queue.
     * @return The value of the removed element, or null if the queue is empty.
     */
    public T dequeue() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty");
        }
        T value = front.data; // Get the value from the front node
        front = front.next;   // Move the front pointer to the next node
        if (front == null) {  // If the queue becomes empty
            rear = null;      // Reset the rear pointer
        }
        size--;
        return value;
    }
    
    /**
     * View the element at the front of the queue without removing it.
     * @return The value at the front of the queue, or null if the queue is empty.
     */
    public T peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty");
        }
        return front.data;
    }
    

       /**
     * Check if the queue is empty.
     * @return True if the queue is empty, false otherwise.
     */
    public boolean isEmpty() {
        return size == 0;
    }
    

    /**
     * Get the current size of the queue.
     * @return The number of elements in the queue.
     */
    public int size() {
        return size;
    }
    
    public void clear() {
        front = rear = null;
        size = 0;
    }

     /**
     * Print all elements in the queue from front to rear.
     */
    public void printQueue() {
        if (isEmpty()) {
            System.out.println("Queue is empty!");
            return;
        }
        Node<T> current = front;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }
}