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

"""
    # BRUTE FORCE
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

            # Time O(n), Space O(n)



    # TWO STACKS
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.minStack[-1]:
                self.minStack.pop()
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1] if self.minStack else None
    
    
        # Time O(1), Space O(n)
    
"""

class MinStack:
    def __init__(self):

        #min set to infinitive
        self.min = float('inf') 
        self.stack = []  #stack

    
    def push(self, x: int) -> None:
        if not self.stack: #if stack is empty
            self.stack.append(0) #append 0, no diference, itslef is the min
            self.min = x #min now is this element x
        else:
            self.stack.append(x - self.min) #diference between x and min
            if x < self.min: #if x is less than min
                self.min = x  #min is x

    def pop(self) -> None:
        if not self.stack: #if stack is empty return nothing
            return IndexError("pop from empty stack")
        
        pop = self.stack.pop() #pop last element
        
        if pop < 0:  #if pop is negative
            self.min = self.min - pop 

    def top(self) -> int:
        top = self.stack[-1]  #last
        if top > 0:
            return top + self.min #if top is positive, return top + min
        else:
            return self.min #if top is negative, return min

    def getMin(self) -> int:
        return self.min
    
#Time O(1), Space O(n)