let arr: number[] = [1, 2, 3, 4, 5];
console.log("Simple console.log:");
console.log(arr)
/*
arr.forEach(function(element:number) {
    console.log(element);
});
*/

console.log("Enhance loop:");
let output = '';
for(let element of arr) {
   output += element + ' ';
}
console.log(output);



console.log("For loop:");
for(let i:number=0; i < arr.length; i++){
    console.log(arr[i])
}

console.log("Double array");
let doubleArray: number[][] = [[], [], []];
console.log(doubleArray);











export{}