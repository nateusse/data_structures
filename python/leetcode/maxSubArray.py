"""
Given an integer array nums, 
find the subarray with the largest sum, 
and return its sum
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums:
            return 0
        max_sum = nums[0]
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                max_sum = max(max_sum, current_sum)
        return max_sum


arr1 = [-2,1,-3,4,-1,2,1,-5,4]
arr2 = [5]
print(Solution().maxSubArray(arr1)) # 6
print(Solution().maxSubArray(arr2)) # 5


"""
KADANE

def maxSubArray(nums):
    max_current = max_global = nums[0]
    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        if max_current > max_global:
            max_global = max_current
    return max_global
"""