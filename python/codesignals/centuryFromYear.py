import math
"""
Given a year, return the century it is in.
 The first century spans from the year 1 up to and including the year 100, 
the second - from the year 101 up to and including the year 200, etc.

"""

class Solution:
    def centuryFromYear(self, year: int) -> int:
        # return math.ceil(year / 100)
        return ( (year // 100) if year % 100 == 0 else ((year // 100)+1))

       

print(Solution().centuryFromYear(1010)) # 11
print(Solution().centuryFromYear(2024)) # 21
