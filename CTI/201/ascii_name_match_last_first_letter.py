"""

Write a program that takes in the 
user's name, which is taken in as input in all lower-case characters.
 If the least significant bit of the ten's place digit of the ASCII
  representation of the last character of the name matches with the 
  least significant bit of the one's 
place digit of the ASCII representation 
of the last character, 
print "Lsb matches: <tens lsb> <ones lsb>, 
otherwise print "Lsb does not match: <tens lsb> 
<ones lsb>".

EJ: anita "Lsb matches: 1 1"
    cloe "Lsb does not match: 
"""

def ascii_name_matches(name):
    last = ord(name[-1])
    lsbLast = last & 1  #del ultimo
    lsbFirst  = (last//10) & 1  #antepenulto
    res = [("Lsb matches: "+ str(lsbLast)+" "+str(lsbFirst))if lsbFirst == lsbLast else ("Lsb does not match: " +str(lsbFirst)+" "+str(lsbLast))]
    return " ".join(res)
    
    
user = input()
print(ascii_name_matches(user))