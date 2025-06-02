package stack;
import java.util.Stack;
/*
* Design a stack class that supports the push, pop, top, and getMin operations.
* MinStack() initializes the stack object.
* void push(int val) pushes the element val onto the stack.
* void pop() removes the element on the top of the stack.
* int top() gets the top element of the stack.
* int getMin() retrieves the minimum element in the stack.
* Each function should run in O(1) time.
*  */



/**
 * MinStack class that supports push, pop, top, and retrieving the minimum element
 * in constant time.
 */
public class MinStack {
/* 
    //BRUTE FORCE
    private Stack<Integer> stack;

    public MinStack() {
        stack = new Stack<>();
    }
    
    public void push(int val) {
        stack.push(val);
    }
    
    public void pop() {
        stack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        Stack<Integer> tmp = new Stack<>();
        int mini = stack.peek();

        while (!stack.isEmpty()) {
            mini = Math.min(mini, stack.peek());
            tmp.push(stack.pop());
        }
        
        while (!tmp.isEmpty()) {
            stack.push(tmp.pop());
        }
        
        return mini;
    }

    //TWO STACKS
    public class MinStack {
        private Stack<Integer> stack;
        private Stack<Integer> minStack;
    
        public MinStack() {
            stack = new Stack<>();
            minStack = new Stack<>();
        }
        
        public void push(int val) {
            stack.push(val);
            if (minStack.isEmpty() || val <= minStack.peek()) {
                minStack.push(val);
            }
        }
        
        public void pop() {
            if (stack.isEmpty()) return;
            int top = stack.pop();
            if (top == minStack.peek()) {
                minStack.pop();
            }
        }
        
        public int top() {
            return stack.peek();
        }
        
        public int getMin() {
            return minStack.peek();
        }
    }
*/
    //ONE STACK OPTMIMIZED
        long min;
        Stack<Long> stack;
    
        public MinStack() {
            stack = new Stack<>();
        }
        
        public void push(int x) {
            if (stack.isEmpty()) {
                stack.push(0L);
                min = x;
            } else {
                stack.push(x - min);
                if (x < min) min = x;
            }
        }
    
        public void pop() {
            if (stack.isEmpty()) return;
            
            long pop = stack.pop();
            
            if (pop < 0) min = min - pop;
        }
    
        public int top() {
            long top = stack.peek();
            if (top > 0) {
                return (int) (top + min);
            } else {
                return (int) min;
            }
        }
    
        public int getMin() {
            return (int) min;
        }
    
}