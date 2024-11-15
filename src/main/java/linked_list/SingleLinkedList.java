package linked_list;

/**
 * Class representing a single node in the linked list.
 */
class Node {
    int data;       // Value of the node
    Node ref;       // Reference to the next node

    /**
     * Constructor to initialize a new node.
     * 
     * @param data The value to be stored in the node.
     */
    public Node(int data) {
        this.data = data;
        this.ref = null;
    }
}

/**
 * Class representing a singly linked list.
 */
public class SingleLinkedList {
    private Node head; // Reference to the head of the linked list

    /**
     * Constructor to initialize an empty linked list.
     */
    public SingleLinkedList() {
        this.head = null;
    }

    /**
     * Prints all the elements of the linked list.
     */
    public void printList() {
        if (head == null) { // Check if the list is empty
            System.out.println("Linked list is empty!");
        } else {
            Node current = head;
            while (current != null) { // Traverse the list
                System.out.print(current.data + " -> ");
                current = current.ref;
            }
            System.out.println("None"); // End of the list
        }
    }

    /**
     * Adds a node at the beginning of the linked list.
     * 
     * @param data The value to be added at the beginning.
     */
    public void addAtBegin(int data) {
        Node newNode = new Node(data); // Create a new node
        newNode.ref = head;            // Link the new node to the current head
        head = newNode;                // Update the head to the new node
    }

    /**
     * Adds a node at the end of the linked list.
     * 
     * @param data The value to be added at the end.
     */
    public void addAtEnd(int data) {
        Node newNode = new Node(data); // Create a new node
        if (head == null) {            // If the list is empty
            head = newNode;
        } else {
            Node current = head;
            while (current.ref != null) { // Traverse to the last node
                current = current.ref;
            }
            current.ref = newNode; // Link the last node to the new node
        }
    }

    /**
     * Adds a node after a specific value in the linked list.
     * 
     * @param data  The value to be added.
     * @param value The value after which the new node will be added.
     */
    public void addAfter(int data, int value) {
        Node current = head;
        while (current != null) { // Traverse the list
            if (current.data == value) { // Find the node with the given value
                break;
            }
            current = current.ref;
        }
        if (current == null) { // If the node with the given value is not found
            System.out.println("Node is not present in the linked list!");
        } else {
            Node newNode = new Node(data); // Create a new node
            newNode.ref = current.ref;    // Link the new node to the next node
            current.ref = newNode;        // Link the current node to the new node
        }
    }

    /**
     * Adds a node before a specific value in the linked list.
     * 
     * @param data  The value to be added.
     * @param value The value before which the new node will be added.
     */
    public void addBefore(int data, int value) {
        if (head == null) { // If the list is empty
            System.out.println("Linked List is empty!");
            return;
        }
        if (head.data == value) { // If the node to add before is the head
            addAtBegin(data);
            return;
        }
        Node current = head;
        while (current.ref != null) { // Traverse the list
            if (current.ref.data == value) { // Find the node before the target
                break;
            }
            current = current.ref;
        }
        if (current.ref == null) { // If the node with the value is not found
            System.out.println("Node is not found!");
        } else {
            Node newNode = new Node(data); // Create a new node
            newNode.ref = current.ref;    // Link the new node to the target node
            current.ref = newNode;        // Link the previous node to the new node
        }
    }

    /**
     * Inserts a node into an empty linked list.
     * 
     * @param data The value to be added.
     */
    public void insertInEmptyList(int data) {
        if (head == null) { // Check if the list is empty
            head = new Node(data); // Create a new node and set it as the head
        } else {
            System.out.println("Linked List is not empty!");
        }
    }

    /**
     * Deletes the first node in the linked list.
     */
    public void deleteBegin() {
        if (head == null) { // If the list is empty
            System.out.println("Linked List is empty, can't delete!");
        } else {
            head = head.ref; // Update the head to the next node
        }
    }

    /**
     * Deletes the last node in the linked list.
     */
    public void deleteEnd() {
        if (head == null) { // If the list is empty
            System.out.println("Linked List is empty, can't delete nodes!");
        } else if (head.ref == null) { // If there is only one node
            head = null; // Set the list to empty
        } else {
            Node current = head;
            while (current.ref.ref != null) { // Traverse to the second last node
                current = current.ref;
            }
            current.ref = null; // Remove the reference to the last node
        }
    }

    /**
     * Deletes a node by its value from the linked list.
     * 
     * @param value The value of the node to delete.
     */
    public void deleteByValue(int value) {
        if (head == null) { // If the list is empty
            System.out.println("Can't delete, Linked List is empty!");
            return;
        }
        if (head.data == value) { // If the node to delete is the head
            head = head.ref; // Update the head
            return;
        }
        Node current = head;
        while (current.ref != null) { // Traverse the list
            if (current.ref.data == value) { // Find the node with the given value
                break;
            }
            current = current.ref;
        }
        if (current.ref == null) { // If the node with the value is not found
            System.out.println("Node is not present!");
        } else {
            current.ref = current.ref.ref; // Remove the node by updating the links
        }
    }

}
