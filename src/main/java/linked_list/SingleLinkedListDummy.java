package linked_list;

/**
 * Class representing a node in a singly linked list.
 */
class ListNode {
    int val;       // The value stored in the node
    ListNode next; // Pointer to the next node in the list

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
 * Class representing a singly linked list with basic operations.
 */
public class SingleLinkedListDummy {
    private ListNode head; // Dummy head node
    private ListNode tail; // Pointer to the last node

    /**
     * Constructor to initialize the linked list.
     * Initializes the linked list with a dummy head node for easier operations.
     */
    public SingleLinkedListDummy () {
        head = new ListNode(-1); // Dummy head node
        tail = head;            // Tail points to the dummy node initially
    }

    /**
     * Inserts a new node with the given value at the end of the linked list.
     *
     * @param val The value to be added to the list.
     */
    public void insertEnd(int val) {
        ListNode newNode = new ListNode(val); // Create a new node
        tail.next = newNode;                  // Link the new node at the end of the list
        tail = newNode;                       // Update the tail pointer
    }

    /**
     * Removes the node at the specified index.
     *
     * @param index The position of the node to remove (0-based index).
     */
    public void remove(int index) {
        int i = 0;
        ListNode curr = head; // Start from the dummy head node

        // Traverse to the node just before the target index
        while (i < index && curr.next != null) {
            i++;
            curr = curr.next;
        }

        // If the node to be removed exists, update the links
        if (curr.next != null) {
            if (curr.next == tail) { // If removing the last node, update tail
                tail = curr;
            }
            curr.next = curr.next.next; // Skip the target node
        }
    }

    /**
     * Prints all the elements in the linked list.
     */
    public void printList() {
        ListNode curr = head.next; // Start from the first real node (skip dummy head)
        while (curr != null) {
            System.out.print(curr.val + " -> ");
            curr = curr.next;
        }
        System.out.println("None"); // End of the list
    }

    
}

