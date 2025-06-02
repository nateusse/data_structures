'''
Given a square of a chessboard. 
If it's a black square, print YES, 
otherwise print NO.


The program receives two integers from 1 to 8
 specifying the column and row number of the square.

 NOTA: UN tablero e ajedrez es 8 X 8

input: 2 numeros (eje x y luego y)
output: "YES" or "NO" if its  a black square , no if white

'''

def  ajedrez_torre(num1, num2):
    
   res = ["YES" if (num1%2!=0 and  num2%2!=0) or  (num1%2==0 and  num2%2==0)  else "NO"]
   return "".join(res)


user1, user2 = int(input()),int(input())
print(ajedrez_torre(user1, user2))