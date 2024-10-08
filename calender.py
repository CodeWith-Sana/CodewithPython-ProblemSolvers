
# Program to display calendar of the given month and year
import calendar
yy = 2024  # year
mm = 10   # month

# display the calendar
print(calendar.month(yy, mm))
# Display the whole calendar for the year  
print(calendar.calendar(yy)) 

# to check if leap year 

def  leapYear(year):
    if(year%4==0):
        return True
    else:
        return False
value  =  2002
if(leapYear(value)==True):
    print("the year is leaf year")
else: 
    print("the year is not leap year")
     