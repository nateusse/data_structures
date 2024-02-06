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


const synonyms = ['fantastic', 'wonderful', 'great'];
//const greetings = [];

/*
for (let i = 0; i < synonyms.length ; i++){
    greetings.push(`Have a ${synonyms[i]} day`)
    console.log(greetings[i]) 
  }
*/

//add new element in fist spot
let newElement = 'new';
for (let i =  arr.length ; i > 0; i--){
//toca mover todo un pasito a la derecha
    
    arr[i] = arr[i - 1]
   
}

arr[0] = newElement;
console.log(arr)


//let arr = ['new', 1, 2, 3, 4, 5]; // your array

// Shift all elements one position to the left
for (let i = 0; i < arr.length - 1; i++){
    arr[i] = arr[i + 1];
}

// Remove the last element
arr.length = arr.length - 1;

console.log(arr); // Output: [1, 2, 3, 4, 5]


const firstNames = ["Jon", "Arya", "Jamie"];
const lastNames = ["Snow", "Stark", "Lannister"];
const places = ["The Wall", "Winterfell", "Kings Landing"];
let hola = [];
const bios = [];
for ( let i = 0; i < firstNames.length; i++){
    hola =  `My name is ${firstNames[i]} ${lastNames[i]} and I am from ${places[i]}`
    bios.push(hola);

}

//Object.values. arra for (leti in object)

let arr1 = [1,2,3,4];
let arr2 = [4];
let arr3 = [4,5,6];
function joinArr (arrs){
 let arrBig
 //duplicate 
}

console.log(joinArr([arr1,arr2, arr3]))


function addingAllTheWeirdStuff(array1, array2){
    // ADD CODE HERE
    //array2 = odd(impar) numbers (%), total += sum
    //arr1 = if ([i] < 10) {[i] + total}
    
    //sECOND PART
      //array2 = even numbers (%), total += sum //arr1 = if ([i] > 10) {[i] + total}
    
    //if (arr2[i] > 20 ) arr[1]+1
    
    
  //create variable totalEve, totalOdd
  // create for arr2.length 
    let sumOdds = 0, sumEven = 0, odds1 , even1
    for (let i = 0; i < array2.length; i++){
      //let  hello = array2[i] % 2 !== 0
     // console.log(hello)
     // if (hello === true) sumOdds += array2[i]
    if(array2[i] % 2 !== 0 ) sumOdds += array2[i] ;
    if(array2[i] % 2 === 0 ) sumEven += array2[i];
    console.log(array1[i] + sumOdds)
   // (array1[i] < 10) ? array1[i] + sumOdds : sumEven += array2[i]; 
      
    
    }
  
    //condicional ood aarr2
    return (sumEven)
  }
  
  // Uncomment these to check your work!                    //1 + 3 + 5 = 9 odd                1+9,          +6 even
  console.log(addingAllTheWeirdStuff([1, 3, 5, 17, 15], [1, 2, 3, 4, 5])); // expected log [10, 12, 14, 23, 21]
  //console.log(addingAllTheWeirdStuff([1, 3, 5, 17, 15, 1], [1, 2, 3, 4, 5, 22])); // expected log [11, 13, 15, 46, 44, 11]
  