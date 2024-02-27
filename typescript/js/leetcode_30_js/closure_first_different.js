/*

Given an integer n, return a counter function. 
This counter function initially returns n and then returns
1 more than the previous value every subsequent time it is called (n, n + 1, n + 2, etc).

*/

/**
 * @param {number} n
 * @return {Function} counter
 */

var createCounter = function (n) { return() =>  n++; };

 console.log(createCounter(10)())
 const counter = createCounter(5)
 console.log(counter()) // 5
 console.log(counter()) // 6
 console.log(counter()) // 7




 
