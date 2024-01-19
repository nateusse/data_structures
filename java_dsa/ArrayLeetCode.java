package java_dsa;

import java.util.HashSet;
import java.util.Set;

public class ArrayLeetCode {
    /*Contain duplicates 
     * Given an integer array nums,
     *  return true if any value appears at least twice in the array, 
     * and return false if every element is distinct.
    */
    public static boolean containsDuplicate(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] == nums[j])
                    return true;
            }
        }
        return false;
    }

    public static boolean containsDuplicateSet(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (seen.contains(num)) //condicional primero 
                return true;
            seen.add(num); //agrergar
        }
        return false;
    }

    /*Valid anagram
     * Given two strings s and t, return true if t is an anagram of s, and false otherwise.

        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
        typically using all the original letters exactly once.
     */
    public boolean isAnagram(String s, String t) {
        return false;
    }
}
