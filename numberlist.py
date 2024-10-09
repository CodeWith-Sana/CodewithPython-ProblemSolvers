number = [12, 3,4,5,7,10,1]
x   = y = number[0]
sum = 0
#to find sum , largest and smallest elemnt in list
for i in number:
    sum += i
    if(i>x):
        i =x
    if(i<x):
        y = i
print(f"SUM: {sum}")
print(f"largest number is :{x} and smallest number is {y}")
#to sort list
number.sort
print(f"sorted list is :{number}")