/*
Write a function createCounter. It should accept an initial integer init. It should return an object with three functions.

The three functions are:

increment() increases the current value by 1 and then returns it.
decrement() reduces the current value by 1 and then returns it.
reset() sets the current value to init and then returns it.
 */

/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */

/*
type Counter = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

function createCounter(init: number): Counter {
    let val:number = init;
     return {
        increment: () => ++val,
        decrement: () => --val,
        reset: () => { val = init; return val; }
    }
};
*/
/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */

class Counter {
    constructor(init) {
      this.init = init;
      this.presentCount = init;
    }
  
    increment() {
      this.presentCount += 1;
      return this.presentCount;
    }
  
    decrement() {
      this.presentCount -= 1;
      return this.presentCount;
    }
  
    reset() {
      this.presentCount = this.init;
      return this.presentCount;
    }
  }
  
  var createCounter = function(init) {
    return new Counter(init);
  };

const counter = createCounter(5)
console.log(counter.increment()); // 6
console.log(counter.reset()); // 5
console.log(counter.decrement()); // 4
