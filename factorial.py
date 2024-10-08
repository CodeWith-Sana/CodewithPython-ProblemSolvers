def factorial_number(num):
    if num ==0:
        return 1
    elif num==1:
        return 1
    else:
        return(num*factorial_number(num-1))

fact =  5
print(factorial_number(fact))