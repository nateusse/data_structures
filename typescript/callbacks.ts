/**
 * @callback Callback
 * @param {number} n
 * @returns {boolean}
 */

//Definir tipo de callback
type Callback = (a: number, b: number) => number;
//type Callback = (str: string) => void;

function calculate(a: number, b: number, callback: Callback): number {
    return callback(a, b);
}

/*function processUserEntry(callback: Callback): void { // callback passed as an argument
   let name: string = "Sexy.";
   callback(name);
}*/

let add: Callback = (a, b) => a + b;
/*function hi(str: string): void {
    console.log("hi " + str);
}*/

console.log(calculate(5, 10, add)); // Outputs: 15