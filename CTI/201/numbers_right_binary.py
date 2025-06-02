
def numbers_right_binary(num):
    list_nums = num.split()
    final =  int(list_nums [-1])
    res1 = format(int(list_nums[0]), '#010b')
    res2 = format(int(list_nums[1]), '#010b')
    res3 = format(int(list_nums[2]), '#010b')
    res4 = format(int(list_nums[3]), '#010b')
    return int(res1[-final-1])+ int(res3[-final-1]) + int(res4[-final-1]) +int(res2[-final-1]) 
    
    
    
   
   
user = input()
print(numbers_right_binary(user))


#2 3 5 6 1

# 2 = 0010 
# 3 = 0011
# 5 = 0101
# 6  = 0110
#a, b , c = int(input()), int(input()), int(input())
#print (int(a>>2), int(b<<2), int(c & 2))
