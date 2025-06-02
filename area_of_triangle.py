"""

Purpose: Learn to use input and output functions of Python to solve a math calculation problem.

Steps:

Read the value for the base of a given triangle from input
Read the value for the height of a given triangle from input
Calculate the area of the triangle
Output the area of the triangle

"""

def areaTraingle(num1, num2):
   return (num1*num2)/2

num1 , num2 = int(input()), int(input())
print(areaTraingle(num1, num2))

