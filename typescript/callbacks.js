/**
 * @callback Callback
 * @param {number} n
 * @returns {boolean}
 */
//type Callback = (str: string) => void;
function calculate(a, b, callback) {
    return callback(a, b);
}
/*function processUserEntry(callback: Callback): void { // callback passed as an argument
   let name: string = "Sexy.";
   callback(name);
}*/
var add = function (a, b) { return a + b; };
/*function hi(str: string): void {
    console.log("hi " + str);
}*/
console.log(calculate(5, 10, add)); // Outputs: 15

const colors = ["red", "yellow", "blue"];
colors[5] = "purple";
//const iterator = colors.keys();
for (const key in colors) {
  console.log(`${key}: ${colors[key]}`);
}
// Output
// 0: red
// 1: yellow
// 2: blue
// 3: undefined
// 4: undefined
// 5: purple



const animals = ["dog", "cat", "tree frog"];

console.log(pluralize(animals)); // should log: ["dogs", "cats", "tree frogs"]
console.log(pluralize(hola))

//como simular encapsulacion clausulas, Symbols o campos de clase privados