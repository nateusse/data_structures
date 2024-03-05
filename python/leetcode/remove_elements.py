"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, 
you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.

"""

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k=0 #pointer 
        for i in range(len(nums)):
            if nums[i] != val:  #si no es igual, agregarlo comienzo
                nums[k] = nums[k] #guia para poer el siguiente valor
                k += 1
                #no else, no ahcemos nada con el match
        return k,nums

print(Solution().removeElement([0,1,2,2,3,0,4,2],2)) # 5, nums = [0,1,4,0,3,_,_,_]
print(Solution().removeElement([3,2,2,3],3)) # 2, nums = [2,2,_,_]     