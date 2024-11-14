"""
Given an integer array nums sorted in non-decreasing 
order, remove the duplicates in-place such that each 
unique element appears only once. 
The relative order of the elements should be kept 
the same. Then return the number of unique elements 
in nums.

Consider the number of unique elements of
 nums to be k, to get accepted, 
 you need to do the following things:

    Change the array nums such that the first k
      elements of nums contain the unique elements 
      in the order they were present in nums initially. 
      The remaining elements of nums are not 
      important as well as the size of nums.
    Return k.

"""

class RemoveDuplicatesSorted:
    """
    Class to remove duplicates from a sorted array in-place.
    """
    
    def remove_duplicates_sorted(self, nums: list[int]) -> int:
        """
        Removes duplicates from the sorted array in-place such that each unique element appears only once.
        Args:
            nums (List[int]): A sorted list of integers.     
        Returns:
            int: The number of unique elements in the array.
        """
        
        # Edge case: If nums is empty, return 0
        if not nums: return 0

        # Pointer to the next unique position
        unique_index = 1

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # Check if the current element is different from the previous one
            if nums[unique_index] != nums[i - 1]:
                # Place the unique element at the next position
                nums[unique_index] = nums[i]
                unique_index += 1  # Increment the position for the next unique element

        # Return the number of unique elements
        return unique_index
