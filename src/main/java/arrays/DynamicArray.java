package arrays;
/**
 * A dynamic array that resizes itself as needed.
 * Provides basic operations such as adding, retrieving, setting, and removing elements.
 *
 * @param <T> the type of elements in this dynamic array
 */
public class DynamicArray<T> {
    private T[] arr;
    private int size;
    private int capacity;

    /**
     * Constructs a new DynamicArray with a default capacity of 10.
     */
    @SuppressWarnings("unchecked")
    public DynamicArray() {
        this.capacity = 10;
        this.arr = (T[]) new Object[capacity];
        this.size = 0;
    }

    /**
     * Adds a new element at the end of the array.
     * Resizes the array if it is full.
     *
     * @param element the element to add
     */
    public void add(T element) {
        if (size == capacity) {
            resize();
        }
        arr[size] = element;
        size++;
    }

    /**
     * Returns the element at the specified index.
     *
     * @param index the index of the element to return
     * @return the element at the specified index
     * @throws IndexOutOfBoundsException if the index is out of range
     */
    public T get(int index) {
        if (index >= size || index < 0) {
            throw new IndexOutOfBoundsException("Index out of range.");
        }
        return arr[index];
    }

    /**
     * Sets a new element at the specified index.
     *
     * @param index   the index of the element to replace
     * @param element the element to be stored at the specified position
     * @throws IndexOutOfBoundsException if the index is out of range
     */
    public void set(int index, T element) {
        if (index >= size || index < 0) {
            throw new IndexOutOfBoundsException("Index out of range.");
        }
        arr[index] = element;
    }

    /**
     * Removes the element at the specified index and shifts elements to the left.
     *
     * @param index the index of the element to remove
     * @throws IndexOutOfBoundsException if the index is out of range
     */
    public void remove(int index) {
        if (index >= size || index < 0) {
            throw new IndexOutOfBoundsException("Index out of range.");
        }
        for (int i = index; i < size - 1; i++) {
            arr[i] = arr[i + 1];
        }
        arr[size - 1] = null;
        size--;
    }

    /**
     * Returns the current size of the array.
     *
     * @return the current number of elements in the array
     */
    public int getSize() {
        return size;
    }

    /**
     * Returns the current capacity of the array.
     *
     * @return the capacity of the array
     */
    public int getCapacity() {
        return capacity;
    }

    /**
     * Doubles the capacity of the array when it reaches full capacity.
     */
    @SuppressWarnings("unchecked")
    private void resize() {
        capacity *= 2;
        T[] newArr = (T[]) new Object[capacity];
        for (int i = 0; i < size; i++) {
            newArr[i] = arr[i];
        }
        arr = newArr;
    }

    /**
     * Prints the elements in the array.
     */
    public void printArray() {
        for (int i = 0; i < size; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}
