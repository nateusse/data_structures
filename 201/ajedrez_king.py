'''
Chess king moves one square in any direction. 
Given two different squares of the chessboard,
 determine whether a king can go from the first 
 square to the second one in a single move.

The program receives four numbers from 1 to 8 
each specifying the column and the row number,
 first two - for the first square, and the last
  two - for the second square. 
  The program should output YES if a 
  king can go from the first square to 
  the second one in a single move or NO otherwise.

input = 4 nums, 2 actual position, 2 future
output =YES , NO string
plan
num 1 solo tiene 2 opciones menor o mayor o igual num, mismo el 2
comparar si num 3 y 4 estan en esa categoria 
pera peracuandro opuesto
'''

def  ajedrez_king(num1, num2, num3, num4):
    
   res = [ "YES" if ((num3 == num1+1) or ( num3 == num1 -1) or (num3==num1) )
   and ((num4 == num2+1) or ( num4 == num2 -1) or (num4==num2) )  else "NO"] #negro
   return "".join(res)

user1, user2, user3, user4 = int(input()),int(input()),int(input()),int(input())
print(ajedrez_king(user1, user2, user3, user4))