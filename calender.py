
# Program to display calendar of the given month and year
import calendar
yy = 1900  # year
mm = 2   # month

# display the calendar
print(calendar.month(yy, mm))
# Display the whole calendar for the year  
# print(calendar.calendar(yy)) 

# to check if leap year 

def  leapYear(year):
    if(year%4==0) and (year%100 !=0):
        return True
    else:
        return False
value  =  1900
if(leapYear(value)==True):
    print("the year is leaf year")
else: 
    print("the year is not leap year")
     