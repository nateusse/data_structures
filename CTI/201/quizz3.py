user_input1 = 21
balance1 = 11

if(user_input1 >= 21 and balance1 > 10):

     print("True")

else:

     print("False")


user_input2 = 20
balance2 = 10 #da false con 10

if(user_input2 >= 21 and balance2 > 10):

     print("True")

else:

     print("False")    

if(3 < 5 or (7 > 9 and 8 != 8)):

    print("True")

else:

    print("False")


if(3 < 5 and (7 > 9 or 8 != 8)):

    print("True")

else:

    print("False")

print("#####################################")

if(True):

    print("One")

    if(False):

         print("Two")

    else: 

        print("Three")

    print("Four")

else: 

    print ("Five")

print("#####################################")
if(False):

    print("One")

    if(False):

        print("Two")

    else: 

        print("Three")

        print("Four")

else: 

    print ("Five")


res= (1234%10)*10+4
print(res//10)