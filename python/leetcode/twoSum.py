"""

Given an array of integers nums, and an integer target,
returns indices of the two numbers such that they add up to target. 
You can assume that each input would have exactly one solution, 
and you may not use the same element twice. 
You can return your answer in order
"""

class Solution: 
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return "sorry papi"


list1 = [1, 7,2,3]
print(Solution().twoSum(list1, 5)) # [0, 2] 1 + 4 = 5