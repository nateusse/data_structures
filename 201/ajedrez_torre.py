'''
Chess rook (torre) moves horizontally
 or vertically. 
 Given two different squares of the chessboard, 
 determine whether a rook can go from the 
 first square to the second one in a single move.

The program receives four numbers from 1 to 8
 each specifying the column and the row number, 
 first two - for the first square, 
 and the last two - for the second square. 
 The program should output YES if a 
 rook can go from the first square to 
 the second one in a single move or NO otherwise.

 NOTA: UN tablero e ajedrez es 8 X 8

input: 4 numeros (2 para posicion actual, eje X luego Y, los otros para final)
output: "YES" or "NO" if can or not go from 1 to other

'''

def  ajedrez_torre(num1, num2, num3, num4):
    
   res = ["YES" if num1==num3 or num2==num4 else "NO"]
   return "".join(res)


user1, user2, user3, user4 = int(input()),int(input()),int(input()),int(input())
print(ajedrez_torre(user1, user2, user3, user4))