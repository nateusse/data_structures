package linked_list;

/**
 * Class representing a single node in a doubly linked list.
 */
class Node {
    int val;      // Value stored in the node
    Node next;    // Pointer to the next node
    Node prev;    // Pointer to the previous node

    /**
     * Constructor to initialize a node with a value.
     * 
     * @param val The value to be stored in the node.
     */
    public Node(int val) {
        this.val = val;
        this.next = null;
        this.prev = null;
    }
}

/**
 * Implementation of a Doubly Linked List with dummy head and tail nodes.
 * Supports insertion and removal at both ends, as well as printing the list.
 */
public class DoubleLinkedList {
    private Node head; // Dummy head node
    private Node tail; // Dummy tail node

    /**
     * Constructor to initialize an empty doubly linked list with dummy nodes.
     */
    public DoubleLinkedList() {
        head = new Node(-1); // Initialize dummy head
        tail = new Node(-1); // Initialize dummy tail
        head.next = tail;    // Link dummy head to dummy tail
        tail.prev = head;    // Link dummy tail to dummy head
    }

    /**
     * Inserts a new node with the given value at the front of the list.
     * 
     * @param val The value to be inserted at the front.
     */
    public void insertFront(int val) {
        Node newNode = new Node(val); // Create a new node
        newNode.prev = head;          // Link new node to dummy head
        newNode.next = head.next;     // Link new node to the first real node
        
        head.next.prev = newNode;     // Update the first real node's previous pointer
        head.next = newNode;          // Update dummy head's next pointer to new node
    }

    /**
     * Inserts a new node with the given value at the end of the list.
     * 
     * @param val The value to be inserted at the end.
     */
    public void insertEnd(int val) {
        Node newNode = new Node(val); // Create a new node
        newNode.next = tail;          // Link new node to dummy tail
        newNode.prev = tail.prev;     // Link new node to the current last real node
        
        tail.prev.next = newNode;     // Update the current last real node's next pointer
        tail.prev = newNode;          // Update dummy tail's previous pointer to new node
    }

    /**
     * Removes the first node from the list.
     * 
     * @throws IllegalStateException if the list is empty.
     */
    public void removeFront() {
        if (head.next == tail) { // Check if the list is empty
            throw new IllegalStateException("List is empty, cannot remove!");
        }
        head.next = head.next.next;   // Move dummy head's next pointer to the second node
        head.next.prev = head;       // Update the new first node's previous pointer
    }

    /**
     * Removes the last node from the list.
     * 
     * @throws IllegalStateException if the list is empty.
     */
    public void removeEnd() {
        if (tail.prev == head) { // Check if the list is empty
            throw new IllegalStateException("List is empty, cannot remove!");
        }
        tail.prev = tail.prev.prev;   // Move dummy tail's previous pointer to the second last node
        tail.prev.next = tail;       // Update the new last node's next pointer
    }

    /**
     * Prints all the values in the list from front to rear.
     * Values are separated by arrows (->).
     */
    public void print() {
        Node curr = head.next; // Start from the first real node (skip dummy head)
        while (curr != tail) { // Traverse until the dummy tail
            System.out.print(curr.val + " -> ");
            curr = curr.next; // Move to the next node
        }
        System.out.println("null"); // Indicate the end of the list
    }

}
