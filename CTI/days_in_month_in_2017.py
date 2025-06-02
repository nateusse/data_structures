"""
Given a month - an integer 
from 1 to 12, print the
number of days in it in the year 2017.


input -> integer 
output -> num days
"""



def days_in_any_month_in_2017(month):
    if(month==2): return ("28")
    elif(month==4 or month==6 or month==9 or month==11):return ("30")
    else: return ("31")





user = int(input())
print(days_in_any_month_in_2017(user))