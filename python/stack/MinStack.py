"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

"""

class MiniStack:

    class MinStack:
        def __init__(self):
            self.stack = []

        def push(self, val: int) -> None:
            self.stack.append(val)

        def pop(self) -> None:
            if self.stack.nonempty():
                self.minStack.pop()  

        def top(self) -> int:
            return self.stack[-1]

        def getMin(self) -> int:
            temporal = []
            mini = self.stack[-1]

            while self.stack.nonempty(): #or len(self.stack) 
                mini = min(mini, self.stack[-1])
                #append in temporary stack last element of stack
                temporal.append(self.stack.pop())
            
            while temporal.nonempty(): #or len(temporal)
                #restore the stack
                self.stack.append(temporal.pop())
        
            return mini