package linked_list;

// Class representing a single node in a doubly linked list
class ListNode {
    int val;           // Value of the node
    ListNode next;     // Pointer to the next node
    ListNode prev;     // Pointer to the previous node

    // Constructor to initialize a new node
    public ListNode(int val) {
        this.val = val;
        this.next = null;
        this.prev = null;
    }
}

// Class representing a doubly linked list
public class DoubleDummyLinkedList {
    private ListNode head;  // Dummy head node
    private ListNode tail;  // Dummy tail node

    // Constructor to initialize the doubly linked list with dummy nodes
    public DoubleDummyLinkedList() {
        head = new ListNode(-1);  // Dummy head node
        tail = new ListNode(-1);  // Dummy tail node
        head.next = tail;         // Connect dummy head to dummy tail
        tail.prev = head;         // Connect dummy tail to dummy head
    }

    /**
     * Inserts a new node with the given value at the front of the list.
     *
     * @param val The value to be inserted.
     */
    public void insertFront(int val) {
        ListNode newNode = new ListNode(val);  // Create a new node
        newNode.prev = head;                   // Link the new node to the dummy head
        newNode.next = head.next;              // Link the new node to the first real node

        head.next.prev = newNode;              // Update the previous pointer of the first real node
        head.next = newNode;                   // Update the next pointer of the dummy head
    }

    /**
     * Inserts a new node with the given value at the end of the list.
     *
     * @param val The value to be inserted.
     */
    public void insertEnd(int val) {
        ListNode newNode = new ListNode(val);  // Create a new node
        newNode.next = tail;                   // Link the new node to the dummy tail
        newNode.prev = tail.prev;              // Link the new node to the current last real node

        tail.prev.next = newNode;              // Update the next pointer of the current last real node
        tail.prev = newNode;                   // Update the previous pointer of the dummy tail
    }

    /**
     * Removes the first node in the list (after the dummy head).
     */
    public void removeFront() {
        if (head.next == tail) { // Check if the list is empty
            System.out.println("List is empty! Nothing to remove.");
            return;
        }
        head.next.next.prev = head;  // Update the previous pointer of the second node
        head.next = head.next.next;  // Update the next pointer of the dummy head
    }

    /**
     * Removes the last node in the list (before the dummy tail).
     */
    public void removeEnd() {
        if (tail.prev == head) { // Check if the list is empty
            System.out.println("List is empty! Nothing to remove.");
            return;
        }
        tail.prev.prev.next = tail;  // Update the next pointer of the second last node
        tail.prev = tail.prev.prev;  // Update the previous pointer of the dummy tail
    }

    /**
     * Prints all the elements in the list from head to tail.
     */
    public void printList() {
        ListNode curr = head.next;  // Start from the first real node
        while (curr != tail) {      // Traverse until the dummy tail
            System.out.print(curr.val + " -> ");
            curr = curr.next;
        }
        System.out.println("None"); // End of the list
    }

    // Main method to test the doubly linked list
    public static void main(String[] args) {
        LinkedList dll = new LinkedList();

        // Insert elements at the front
        dll.insertFront(10);
        dll.insertFront(20);

        // Insert elements at the end
        dll.insertEnd(5);
        dll.insertEnd(1);

        // Print the list
        System.out.println("Initial list:");
        dll.printList(); // Output: 20 -> 10 -> 5 -> 1 -> None

        // Remove elements from the front and end
        dll.removeFront();
        System.out.println("\nAfter removing front:");
        dll.printList(); // Output: 10 -> 5 -> 1 -> None

        dll.removeEnd();
        System.out.println("\nAfter removing end:");
        dll.printList(); // Output: 10 -> 5 -> None
    }
}

