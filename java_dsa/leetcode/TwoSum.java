package java_dsa.leetcode;

import java.util.Arrays;

/*Given an array of integers nums, and an integer target,
returns indices of the two numbers such that they add up to target. 
You can assume that each input would have exactly one solution, 
and you may not use the same element twice. 
You can return your answer in order

 */

public class TwoSum {
    public static int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{}; // No solution found
    }

    public static void main(String[] args) {
        int[] arr = {1, 7,2,3};
        System.out.print(Arrays.toString(twoSum(arr,5)));
       
    }
}




