"""
Why in ts: 
twoSum(nums: number[], target: number): number[] {
        for (let i = 0; i < nums.length; i++) {
            for (let j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] === target) {
                    return [i, j];
                }
            }
        }
        throw new Error("No solution found");
    }

but in python the range is:

    for i in range(len(nums)):
            for j in range(i+1, len(nums)):
            
The range(n - 1) is used because the inner loop starts from i + 1.

This is a common pattern when you want to compare each element in 
the list with every other element that comes after it.

If i went up to n, then in the last iteration of the outer loop, 
i would be the last index of the list. 
Then i + 1 in the inner loop would be out of range, 
because there are no elements after the last element in the list.

By stopping the outer loop at n - 1, 
you ensure that i + 1 is always a valid index in the list, 
and you avoid an out-of-range error.

"""