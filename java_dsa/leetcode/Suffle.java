package java_dsa.leetcode;

import java.util.Arrays;
/* 
Given the array nums,
consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]
Return the array in the form [x1,y1,x2,y2,...,xn,yn]
*/
public class Suffle {
    public static int[] shuffle(int[] nums, int n) {
        
        int len = nums.length;
		
		// to store the pair of numbers in right half of the original array
        for(int i = n; i < len; i++) {
            nums[i] = (nums[i] * 1024) + nums[i - n];
        }
        
        int index = 0;
		// to retrive values from the pair of numbers and placing those retrieved value at their desired position
        for(int i = n; i < len; i++, index += 2) {
            nums[index] = nums[i] % 1024;
            nums[index + 1] = nums[i] / 1024;
        }
        
        return nums;
    }

    public static void main(String[] args) {
        int[] list1 = {1,2,3,4, 10,11,12,13};
        int n = 4;
        System.out.print(Arrays.toString(Suffle.shuffle(list1, n)));
       
    }
}


