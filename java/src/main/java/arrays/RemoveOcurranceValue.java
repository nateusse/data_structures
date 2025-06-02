package arrays;

/*Given an integer array nums and an integer val, 
remove all occurrences of val in nums in-place.
 The order of the elements may be changed. 
 Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, 
to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums 
    contain the elements which are not equal to val. 
    The remaining elements of nums are not important as well as the size of nums.
    Return k.
 */

public class RemoveOcurranceValue {

   /**
     * Removes all occurrences of val from the array nums in-place.
     * The first k elements of nums will contain the elements not equal to val.
     * 
     * @param nums An array of integers.
     * @param val The integer value to remove from the array.
     * @return The number of elements in nums that are not equal to val.
     */
    public int removeOcurrentElement(int[] nums, int val) {
        int unique_index = 0; // Pointer for the position to place the next element that is not equal to val
        
        // Iterate through the array
        for (int i = 0; i < nums.length; i++) {
            // If the current element is not equal to val, move it to position k
            if (nums[i] != val) {
                nums[unique_index ] = nums[i];
                unique_index ++; // Increment k to track the number of elements not equal to val
            }
        }

        // Return the count of elements that are not equal to val
        return unique_index ;
    }
    
}
