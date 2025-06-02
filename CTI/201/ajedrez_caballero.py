'''
Chess knight can move to a square that is two
 squares away horizontally and one square vertically,
  or two squares vertically and 
  one square horizontally. 
  The complete move, therefore,
   looks like the letter L.
Given two different squares of the chessboard,
determine whether a knight can go from the first 
square to the second one in a single move.

 

The program receives four numbers from 1 to 8
 each specifying the column and the row number, 
 first two - for the first square, 
 and the last two - for the second square. 
 The program should output YES if a knight 
 can go from the first square to the second 
 one in a single move or NO otherwise.
'''

def  ajedrez_caballero(num1, num2, num3, num4):
    
    res = ["YES" if (num3 == num1+1 or num3 == num1-1 ) and (num4 == num2+2 or num4 == num2-2 ) or (num4 == num2+1 or num4 == num2-1 ) and (num3 == num1+2 or num3 == num1-2 ) else "NO"]
    return "".join(res)
    

user1, user2, user3, user4 = int(input()),int(input()),int(input()),int(input())
print(ajedrez_caballero(user1, user2, user3, user4))