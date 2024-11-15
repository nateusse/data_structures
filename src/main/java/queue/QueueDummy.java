package queue;

/**
 * Class representing a single node in a singly linked list.
 */
class ListNode {
    int val;        // Value stored in the node
    ListNode next;  // Pointer to the next node

    /**
     * Constructor to initialize a node with a value.
     *
     * @param val The value to store in the node.
     */
    public ListNode(int val) {
        this.val = val;
        this.next = null;
    }
}

/**
 * Class representing a queue implemented using a singly linked list.
 */
class QueueDummy {
    private ListNode left;  // Points to the front of the queue
    private ListNode right; // Points to the rear of the queue

    /**
     * Constructor to initialize an empty queue.
     */
    public QueueDummy() {
        this.left = null;  // Initialize the front pointer
        this.right = null; // Initialize the rear pointer
    }

    /**
     * Add an element to the end of the queue.
     *
     * @param val The value to be added to the queue.
     */
    public void enqueue(int val) {
        ListNode newNode = new ListNode(val); // Create a new node

        if (right != null) { // If the queue is not empty
            right.next = newNode; // Link the new node to the current rear
            right = newNode;      // Update the rear pointer to the new node
        } else { // If the queue is empty
            left = right = newNode; // Both pointers point to the new node
        }
    }

    /**
     * Remove and return the front element of the queue.
     *
     * @return The value of the removed element, or -1 if the queue is empty.
     */
    public int dequeue() {
        if (left == null) { // If the queue is empty
            System.out.println("Queue is empty!");
            return -1; // Indicate an empty queue
        }

        int val = left.val;     // Store the value of the front node
        left = left.next;       // Move the front pointer to the next node

        if (left == null) {     // If the queue becomes empty after removal
            right = null;       // Reset the rear pointer
        }
        return val;
    }

    /**
     * Print all elements in the queue from front to rear.
     */
    public void print() {
        ListNode cur = left; // Start from the front of the queue
        while (cur != null) {
            System.out.print(cur.val + " -> ");
            cur = cur.next;
        }
        System.out.println("None"); // Indicate the end of the queue
    }

   
}
