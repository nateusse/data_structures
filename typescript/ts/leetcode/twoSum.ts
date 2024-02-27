class Solution {
    twoSum(nums: number[], target: number): number[] | undefined {
        let map: { [key: number]: number } = {};
        for (let i = 0; i < nums.length; i++) {
            if (nums[i] in map) {
                return [map[nums[i]], i];
            } else {
                map[target - nums[i]] = i;
            }
        }
    }
}

console.log(new Solution().twoSum([1, 7, 2, 3], 5));  // Outputs: [0, 2]
console.log(new Solution().twoSum([2, 0, 7, 3], 9))