package arrays;

/* Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, 
to get accepted, you need to do the following things:

Change the array nums such that the first k elements 
of nums contain the unique elements 
in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
*/

/**
 * Class to remove duplicates from a sorted array in-place.
 */
public class RemoveDuplicatesSorted {
    
    /**
     * Removes duplicates from the sorted array in-place so that each unique element appears only once.
     * The method modifies the array so that the first k elements contain the unique elements.
     * 
     * @param nums A sorted array of integers.
     * @return The number of unique elements in the array.
     */
    public int removeDuplicates(int[] nums) {
        // Edge case: If the array is empty, return 0
        if (nums == null || nums.length == 0) {
            return 0;
        }

        // Pointer to track the next position for a unique element
        int uniqueIndex = 1;

        // Iterate through the array starting from the second element
        for (int i = 1; i < nums.length; i++) {
            // Check if the current element is different from the previous unique element
            if (nums[i] != nums[uniqueIndex - 1]) {
                // Place the unique element at the next position
                nums[uniqueIndex] = nums[i];
                uniqueIndex++;  // Increment the position for the next unique element
            }
        }

        // Return the number of unique elements
        return uniqueIndex;
    }
}
