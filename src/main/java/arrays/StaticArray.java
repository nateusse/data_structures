package arrays;

/**
 * A type-safe StaticArray class to simulate a fixed-size array with basic operations.
 * Provides methods to add, retrieve, set, remove, and print elements while maintaining type safety.
 *
 * @param <T> the type of elements in this array
 */
public class StaticArray<T> {
    private final T[] arr;
    private final int capacity;
    private int length;

    /**
     * Constructs a StaticArray with a specified capacity.
     *
     * @param capacity the fixed capacity of the array
     */
    @SuppressWarnings("unchecked")
    public StaticArray(int capacity) {
        this.capacity = capacity;
        this.arr = (T[]) new Object[capacity];
        this.length = 0;
    }

    /**
     * Adds an element at the next open position if there is capacity.
     *
     * @param element the element to be added
     * @throws ArrayIndexOutOfBoundsException if the array is full
     */
    public void add(T element) {
        if (length < capacity) {
            arr[length] = element;
            length++;
        } else {
            throw new ArrayIndexOutOfBoundsException("Array is full");
        }
    }

    /**
     * Returns the element at a specific index.
     *
     * @param index the index of the element to return
     * @return the element at the specified index
     * @throws IndexOutOfBoundsException if the index is out of range
     */
    public T get(int index) {
        if (index < 0 || index >= length) {
            throw new IndexOutOfBoundsException("Index out of range.");
        }
        return arr[index];
    }

    /**
     * Sets a new element at a specific index.
     *
     * @param index the index of the element to replace
     * @param element the element to be stored at the specified position
     * @throws IndexOutOfBoundsException if the index is out of range
     */
    public void set(int index, T element) {
        if (index < 0 || index >= length) {
            throw new IndexOutOfBoundsException("Index out of range.");
        }
        for (int i = length - 1; i > index - 1; i--) {
            arr[index] = arr[index - 1];
        }
        arr[index] = element;
    }

    /**
     * Removes the last element if the array is not empty.
     *
     * @throws ArrayIndexOutOfBoundsException if the array is empty
     */
    public void removeLast() {
        if (length > 0) {
            arr[length - 1] = null;
            length--;
        } else {
            throw new ArrayIndexOutOfBoundsException("Array is empty");
        }
    }

    /**
     * Removes an element at a specific index, shifting elements to fill the gap.
     *
     * @param index the index of the element to remove
     * @throws IndexOutOfBoundsException if the index is out of range
     */
    public void removeMiddle(int index) {
        if (index < 0 || index >= length) {
            throw new IndexOutOfBoundsException("Index out of range.");
        }
        // Shift elements to the left starting from the specified index
        for (int i = index; i < length - 1; i++) {
            arr[i] = arr[i + 1];
        }
        // Clear the last element and reduce the length
        arr[length - 1] = null;
        length--;
    }

    /**
     * Returns the current number of elements in the array.
     *
     * @return the current number of elements
     */
    public int getLength() {
        return length;
    }

    /**
     * Returns the fixed capacity of the array.
     *
     * @return the capacity of the array
     */
    public int getCapacity() {
        return capacity;
    }

    /**
     * Prints all elements in the array up to the current length.
     */
    public void printArray() {
        for (int i = 0; i < length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}
