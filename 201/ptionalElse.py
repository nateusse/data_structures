total = int(input())
while total >=60:
    print ("Pass")
    print (" Please insert total:" + str(int(input())))
print ("No pass")



# Function to convert number into string
# Switcher is dictionary data type here
total = int(input())
switcher = {
    0: "Pass",
    1: "No pass",
}
if total >=60:
    print(switcher.get(0))
print(switcher.get(1))