'''
Given two squares of a chessboard.
 If they are painted in the same color, 
 print YES, otherwise print NO.


The program receives four integers from 1 to 8, 
each specifying the column and row number,
 first two - for the first square, and then the last two
  - for the second square.

'''

def  ajedrez_same_color(num1, num2, num3, num4):
    
   res = [ "YES" if ((num1 + num2) % 2 == 0) and ((num3 + num4) % 2 == 0 ) 
   or ((num1 + num2) % 2 != 0) and ((num3 + num4) % 2 != 0 )  else "NO"] #negro
   return "".join(res)

user1, user2, user3, user4 = int(input()),int(input()),int(input()),int(input())
print(ajedrez_same_color(user1, user2, user3, user4))