import unittest
from python.arrays.StaticArray import StaticArray

class TestStaticArray(unittest.TestCase):

    def setUp(self):
        self.array = StaticArray(5)  # Create a StaticArray with capacity 5

    def test_add_and_get(self):
        self.array.add(10)
        self.array.add(20)
        self.array.add(30)
        self.assertEqual(self.array.get(0), 10)
        self.assertEqual(self.array.get(1), 20)
        self.assertEqual(self.array.get(2), 30)

    def test_add_beyond_capacity(self):
        self.array.add(1)
        self.array.add(2)
        self.array.add(3)
        self.array.add(4)
        self.array.add(5)
        with self.assertRaises(IndexError):
            self.array.add(6)  # Exceeds capacity

    def test_set_and_get(self):
        self.array.add(10)
        self.array.add(20)
        self.array.set(1, 50)
        self.assertEqual(self.array.get(1), 50)

    def test_remove_last(self):
        self.array.add(10)
        self.array.add(20)
        self.array.remove_last()
        self.assertEqual(self.array.get_length(), 1)
        self.assertEqual(self.array.get(0), 10)

    def test_remove_last_empty_array(self):
        with self.assertRaises(IndexError):
            self.array.remove_last()  # Should raise an error on an empty array

    def test_get_invalid_index(self):
        self.array.add(10)
        with self.assertRaises(IndexError):
            self.array.get(2)  # Out of range

    def test_set_invalid_index(self):
        self.array.add(10)
        with self.assertRaises(IndexError):
            self.array.set(2, 20)  # Out of range

    def test_get_length_and_capacity(self):
        self.assertEqual(self.array.get_length(), 0)
        self.assertEqual(self.array.get_capacity(), 5)
        self.array.add(10)
        self.assertEqual(self.array.get_length(), 1)

if __name__ == "__main__":
    unittest.main()
