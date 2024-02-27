"""

Given an array of integers nums, and an integer target,
returns indices of the two numbers such that they add up to target. 
You can assume that each input would have exactly one solution, 
and you may not use the same element twice. 
You can return your answer in order


class Solution: 
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        print(len(nums))
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return ("sorry papi")


        def twoSum(nums, target):
            numMap = {}
            for i, num in enumerate(nums):
                complement = target - num
                if complement in numMap:
                    return [hashMap[complement], i]
                numMap[num] = i
            return []
    
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_table = {}
        for i in range(len(nums)):
            if nums[i] in hash_table:
                return [hash_table[nums[i]], i]
            else:
                hash_table[target - nums[i]] = i
                

print(Solution().twoSum([1, 7,2,3], 5)) # [0, 2] 1 + 4 = 5
print(Solution().twoSum([2,0,7,3], 9)) # [0, 2] 1 + 4 = 5