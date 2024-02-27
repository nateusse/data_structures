/*
Given the array nums,
consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]
Return the array in the form [x1,y1,x2,y2,...,xn,yn]
*/

function reshuffle(nums: number[], n: number): number[] {
    let result: number[] = [];
    for (let i = 0; i < n; i++) {
        result.push(nums[i], nums[i + n]);
    }
    return result;
}

let nums: number[] = [2, 5, 1, 3, 4, 7];
let n: number = 3;
console.log(reshuffle(nums, n));  // Outputs: [2, 1, 5, 3, 1, 7]s