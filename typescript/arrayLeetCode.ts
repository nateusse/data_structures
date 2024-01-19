/*Contain duplicates 
    Given an integer array nums,
    return true if any value appears at least twice in the array, 
    and return false if every element is distinct.

function containsDuplicate(nums: number[]): boolean {
    for (let i:number = 0; i < nums.length - 1 ; i++){
        for (let j:number = i + 1; j < nums.length ; j++){
            if (nums[i] === nums[j]){return true;}
        }
        
    }
    return false;
};


console.log(containsDuplicate([1,2,3,1])) //true
console.log(containsDuplicate([1,2,3])) //false

*/
/*
function containsDuplicateSet(nums: number[]): boolean {
    const set = new Set<number>(nums);
    return (set.size < nums.length);
};

console.log(containsDuplicateSet([1,2,3,1]))
*/


/*Anagram*/
const validAnagram = (s:string, t:string): string => {

    let res = s.split("").sort().join() === t.split("").sort().join()
    //split -- strring into array, sport array , join into string, no mas array
    return "fin";
};


console.log(validAnagram("ana", "hola"));
//console.log(validAnagram("s", "s"));