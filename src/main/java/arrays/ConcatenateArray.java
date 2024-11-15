package arrays;


/*
  Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
  Specifically, ans is the concatenation of two nums arrays.
Return the array ans.
 */
public class ConcatenateArray {

    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] ans = new int[2 * n];

        // Fill the first and second halves of ans with nums
        for (int i = 0; i < n; i++) {
            ans[i] = nums[i];       // First half
            ans[i + n] = nums[i];   // Second half
        }

        return ans;
    }


    /* 
    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] ans = new int[2 * n];

        // Copy nums into the first half of ans
        System.arraycopy(nums, 0, ans, 0, n);
        
        // Copy nums into the second half of ans
        System.arraycopy(nums, 0, ans, n, n);

        return ans;
    }
    */
}
