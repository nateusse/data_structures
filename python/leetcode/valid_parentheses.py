"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
 determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

(parentesis) {curly brakets} [brackets] On for stack and for 1s per char
"""


class Solution:
    def isValid(self, s: str) -> bool:
        #I can also check if len is odd and return Flase
        stack = []
        closeToOpen = {")":"(", "]": "[","}":"{"}
        for close in s:
            #check if key is closing pare
            if close in closeToOpen:
                #check if not empty stack and is the last of the stack
                #is the parentehis we need
                if stack and stack[-1] == closeToOpen[close]: 
                    #si match, remover deel stack
                    stack.pop()
                else: return False 
                #appen cuantos quiera
            else:
                stack.append(close)
        #si no hay anda en el stack True, matches.        
        return True if not stack else False



print(Solution().isValid("()")) # true
print(Solution().isValid("()[]{}")) # true
print(Solution().isValid( "(]")) # false
print(Solution().isValid( "([)]")) # false no order