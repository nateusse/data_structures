package arrays;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Test class for StaticArray.
 */
public class StaticArrayTest {
    private StaticArray<Integer> staticArray;

    @BeforeEach
    public void setUp() {
        staticArray = new StaticArray<>(5);
    }

    @Test
    public void testAddAndGet() {
        staticArray.add(10);
        staticArray.add(20);
        staticArray.add(30);
        assertEquals(10, staticArray.get(0));
        assertEquals(20, staticArray.get(1));
        assertEquals(30, staticArray.get(2));
    }

    @Test
    public void testSet() {
        staticArray.add(10);
        staticArray.add(20);
        staticArray.set(1, 50);
        assertEquals(50, staticArray.get(1));
    }

    @Test
    public void testRemoveLast() {
        staticArray.add(10);
        staticArray.add(20);
        staticArray.add(30);
        staticArray.removeLast();
        assertEquals(2, staticArray.getLength());
        assertEquals(20, staticArray.get(1));
    }

    @Test
    public void testGetLengthAndCapacity() {
        assertEquals(0, staticArray.getLength());
        assertEquals(5, staticArray.getCapacity());
        staticArray.add(10);
        staticArray.add(20);
        assertEquals(2, staticArray.getLength());
    }

    @Test
    public void testAddBeyondCapacity() {
        staticArray.add(1);
        staticArray.add(2);
        staticArray.add(3);
        staticArray.add(4);
        staticArray.add(5);
        assertThrows(ArrayIndexOutOfBoundsException.class, () -> staticArray.add(6));
    }

    @Test
    public void testGetInvalidIndex() {
        staticArray.add(10);
        assertThrows(IndexOutOfBoundsException.class, () -> staticArray.get(5));
    }

    @Test
    public void testSetInvalidIndex() {
        staticArray.add(10);
        assertThrows(IndexOutOfBoundsException.class, () -> staticArray.set(5, 20));
    }

    @Test
    public void testRemoveLastFromEmptyArray() {
        assertThrows(ArrayIndexOutOfBoundsException.class, () -> staticArray.removeLast());
    }
}
