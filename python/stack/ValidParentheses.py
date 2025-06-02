"""
Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

"""

class ValidParentheses:


    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen:  # Es un paréntesis de cierre
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()  # Elimina el último abierto si coincide
                else:
                    return False  # No coincide o no hay abierto
            else:  # Es un paréntesis de apertura
                stack.append(c)

        return not stack  # La pila debe estar vacía si es válido
