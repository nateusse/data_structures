"""
Given an integer array nums, 
find the subarray with the largest sum, 
and return its sum

"""

#brute force
class Solution:
    def maxSubArray(self, nums):
        ans = -inf
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                ans = max(ans, cur_sum)
        return ans
    
#Memizacion
class Solution:
    def maxSubArray(self, nums):
        @cache
        def solve(i, must_pick):
            if i >= len(nums): return 0 if must_pick else -inf
            return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
        return solve(0, False)

#Kadane dinamic
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        if not nums:
            return 0

        cur_sum = max_sum = nums[0]
        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)
        
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

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sumMax = current = nums[0]
        
        for i in range(len(nums)-1):
            current = max(current+nums[i+1], nums[i+1])
            sumMax = max(current, sumMax)
        
        return sumMax