"""
Given a positive integer N, print the numbers from 1 to N.
But for multiples of 3 print “Fizz” instead of the number.
For the multiples of 5, print “Buzz” instead of the number.
For numbers which are multiple of 3 and 5 both, print “FizzBuzz” instead of the number.


"""



#separate newLines is  , sep="\n"
#"Text"*(not i%3)
# * para que no me salga  <map object at 0x000002111110AAD0>
# NOt es para negar 
# map itreracion, map(fun, iter) La funcion es lambda
#lambda arguments MUCHOS : expression 1


total = int(input())
print(*map(lambda i: 'Fizz'*(not i%3)+'Buzz'*(not i%5) or i, range(total)),sep="\n")

