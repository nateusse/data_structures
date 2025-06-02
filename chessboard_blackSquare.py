"""
Read the two numbers from input for the column and row number of the square in a chessboard. 
If it's a black square, print YES, otherwise print NO.
"""

def chess_blackSquare(num1, num2):
    return ("YES" if (num1%2==num2%2) else "NO")

num1 , num2 = int(input()), int(input())
print(chess_blackSquare(num1, num2))