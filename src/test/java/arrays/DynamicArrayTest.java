package arrays;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Test class for DynamicArray.
 */
public class DynamicArrayTest {
    private DynamicArray<Integer> dynamicArray;

    @BeforeEach
    public void setUp() {
        dynamicArray = new DynamicArray<>();
    }

    @Test
    public void testAddAndGet() {
        dynamicArray.add(10);
        dynamicArray.add(20);
        dynamicArray.add(30);
        assertEquals(10, dynamicArray.get(0));
        assertEquals(20, dynamicArray.get(1));
        assertEquals(30, dynamicArray.get(2));
    }

    @Test
    public void testSet() {
        dynamicArray.add(10);
        dynamicArray.add(20);
        dynamicArray.set(1, 50);
        assertEquals(50, dynamicArray.get(1));
    }

    @Test
    public void testRemove() {
        dynamicArray.add(10);
        dynamicArray.add(20);
        dynamicArray.add(30);
        dynamicArray.remove(1);
        assertEquals(2, dynamicArray.getSize());
        assertEquals(30, dynamicArray.get(1));
    }

    @Test
    public void testGetSizeAndCapacity() {
        assertEquals(0, dynamicArray.getSize());
        assertEquals(10, dynamicArray.getCapacity());
        dynamicArray.add(10);
        dynamicArray.add(20);
        assertEquals(2, dynamicArray.getSize());
        assertEquals(10, dynamicArray.getCapacity());
    }

    @Test
    public void testAddBeyondCapacity() {
        for (int i = 0; i < 10; i++) {
            dynamicArray.add(i);
        }
        assertEquals(10, dynamicArray.getSize());
        assertEquals(10, dynamicArray.getCapacity());

        dynamicArray.add(10);
        assertEquals(11, dynamicArray.getSize());
        assertEquals(20, dynamicArray.getCapacity()); // Capacity should double
    }

    @Test
    public void testGetInvalidIndex() {
        dynamicArray.add(10);
        assertThrows(IndexOutOfBoundsException.class, () -> dynamicArray.get(5));
    }

    @Test
    public void testSetInvalidIndex() {
        dynamicArray.add(10);
        assertThrows(IndexOutOfBoundsException.class, () -> dynamicArray.set(5, 20));
    }

    @Test
    public void testRemoveInvalidIndex() {
        dynamicArray.add(10);
        assertThrows(IndexOutOfBoundsException.class, () -> dynamicArray.remove(5));
    }
}
