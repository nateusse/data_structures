'''
Chess queen moves horizontally, 
vertically or diagonally in any number of squares. 
Given two different squares of the chessboard, 
determine whether a queen can go from 
the first square to the second one in a single move.

The program receives four numbers from 1 to 8 
each specifying the column and the row number,
 first two - for the first square, 
 and the last two - for the second square. 
 The program should output YES if a queen 
 can go from the first square to the second 
 one in a single move or NO otherwise.
'''

def  ajedrez_reina(num1, num2, num3, num4):
    
    res = ["YES" if (num1 == num3 or num2== num4) or 
    (abs(num1 - num3 ) == abs (num2 - num4)) else "NO"]
    return "".join(res)
    

user1, user2, user3, user4 = int(input()),int(input()),int(input()),int(input())
print(ajedrez_reina(user1, user2, user3, user4))