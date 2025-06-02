'''
Given an array nums containing n 
distinct numbers in the range [0, n], 
return the only number in the range 
that is missing from the array..

Input - array with nums
output - num
matching: for, len

Plan:
recibir array negativos?
ordenar array
do a while loop itterate puntero con vecino
if missing last one? add one

Una solucion con for )(n)
def  return_missing_num_array(array):
    sorted_array = sorted(array)
    res = [item for item in range(sorted_array[0], (sorted_array[-1]+1)) if item not in sorted_array]
    if res == []: return (sorted_array[-1]+1)
    return res[0]
    

#user=list(input())
print(return_missing_num_array([2,4]))

'''


def  return_missing_num_array(integers):
    suma = sum(integers)
    res =   (len(integers)*(len(integers)+1)) //2
    givensum = 0
    for num in integers:
        givensum = givensum + num
    return (res- suma)

#user=list(input())
print(return_missing_num_array([3,4,6]))