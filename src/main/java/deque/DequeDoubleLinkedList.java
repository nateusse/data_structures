package deque;

/**
 * Class representing a doubly linked list node.
 */
class Node<T> {
    T data;       // Data stored in the node
    Node<T> next; // Pointer to the next node
    Node<T> prev; // Pointer to the previous node

    public Node(T data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

/**
 * Implementation of a Deque (Double-Ended Queue) using a Doubly Linked List.
 */
public class DequeDoubleLinkedList<T> {
    private Node<T> head; // Points to the front of the deque
    private Node<T> tail; // Points to the rear of the deque
    private int size;     // Tracks the number of elements in the deque

    /**
     * Constructor to initialize an empty deque.
     */
    public DequeDoubleLinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    /**
     * Add an element to the rear of the deque.
     * @param value The value to add.
     */
    public void append(T value) {
        Node<T> newNode = new Node<>(value);
        if (tail == null) { // If the deque is empty
            head = tail = newNode;
        } else {
            tail.next = newNode;
            newNode.prev = tail;
            tail = newNode;
        }
        size++;
    }

    /**
     * Add an element to the front of the deque.
     * @param value The value to add.
     */
    public void appendLeft(T value) {
        Node<T> newNode = new Node<>(value);
        if (head == null) { // If the deque is empty
            head = tail = newNode;
        } else {
            newNode.next = head;
            head.prev = newNode;
            head = newNode;
        }
        size++;
    }

    /**
     * Remove and return the element from the rear of the deque.
     * @return The value of the removed element.
     * @throws IllegalStateException if the deque is empty.
     */
    public T pop() {
        if (tail == null) {
            throw new IllegalStateException("Deque is empty!");
        }
        T value = tail.data;
        if (head == tail) { // If there's only one element
            head = tail = null;
        } else {
            tail = tail.prev;
            tail.next = null;
        }
        size--;
        return value;
    }

    /**
     * Remove and return the element from the front of the deque.
     * @return The value of the removed element.
     * @throws IllegalStateException if the deque is empty.
     */
    public T popLeft() {
        if (head == null) {
            throw new IllegalStateException("Deque is empty!");
        }
        T value = head.data;
        if (head == tail) { // If there's only one element
            head = tail = null;
        } else {
            head = head.next;
            head.prev = null;
        }
        size--;
        return value;
    }

    /**
     * Check if the deque is empty.
     * @return True if the deque is empty, false otherwise.
     */
    public boolean isEmpty() {
        return size == 0;
    }

    /**
     * Get the current size of the deque.
     * @return The number of elements in the deque.
     */
    public int getSize() {
        return size;
    }

    /**
     * Print all elements in the deque from front to rear.
     */
    public void printDeque() {
        Node<T> current = head;
        while (current != null) {
            System.out.print(current.data + " <-> ");
            current = current.next;
        }
        System.out.println("null");
    }

    /**
     * Main method to demonstrate the Deque operations.
     */
}
