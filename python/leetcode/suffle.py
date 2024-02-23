"""
Given the array nums,
consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]
Return the array in the form [x1,y1,x2,y2,...,xn,yn]
"""

class Solution: 
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i+n])
        return result


list1 = [1,2,3,4, "a","b","c", "d"]
n = 4
print(Solution().shuffle(list1, n)) # [1, "a", 2, "b", 3, "c", 4, "d"]