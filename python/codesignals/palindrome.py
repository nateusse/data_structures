"""
Given the string, check if it is a palindrome.
Hacer minuscula, mayuscula y reversar

Como poner en minusculas un texto, como reversar un string
"""

class Solution:
     def palindrome(self, word: str) -> bool:
        pal = word[::-1] == word
        return (pal)
       
print(Solution().palindrome("feo"))
print(Solution().palindrome("01010")) # 11
print(Solution().palindrome("aka")) # 21


s = "holas_23*#(@#)ISPLS"
print(s.lower())