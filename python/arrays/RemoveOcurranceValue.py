"""
Given an integer array nums and an integer val,
 remove all occurrences of val in nums in-place. 
 The order of the elements may be changed.
   Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are 
not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements 
which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

"""

class RemoveOcurranceValue:
    """
    Class to remove all occurrences of a value from an array in-place.
    """
    
    def remove_ocurrance_value(self, nums: list[int], val: int) -> int:
        """
        Removes all occurrences of a value from the array in-place.
        Args:
            nums (List[int]): A list of integers.
            val (int): The value to remove from the array.
        Returns:
            int: The number of elements in the array which are not equal to val.
        """
        
        # Edge case: If nums is empty, return 0
        if not nums: return 0

        # Pointer to the next position for the elements which are not equal to val
        unique_index = 0

        # Iterate through the array
        for i in range(len(nums)):
            # Check if the current element is not equal to val
            if nums[i] != val:
                # Place the element which is not equal to val at the next position
                nums[unique_index] = nums[i]
                unique_index += 1  # Increment the position for the next element which is not equal to val

        # Return the number of elements in the array which are not equal to val
        return unique_index