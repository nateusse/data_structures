"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var arr = [1, 2, 3, 4, 5];
console.log("Simple console.log:");
console.log(arr);
/*
arr.forEach(function(element:number) {
    console.log(element);
});
*/
console.log("Enhance loop:");
var output = '';
for (var _i = 0, arr_1 = arr; _i < arr_1.length; _i++) {
    var element = arr_1[_i];
    output += element + ' ';
}
console.log(output);
console.log("For loop:");
for (var i = 0; i < arr.length; i++) {
    console.log(arr[i]);
}
console.log("Double array");
var doubleArray = [[], [], []];
console.log(doubleArray);
