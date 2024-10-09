def factorial_number(num):
    if (num ==0 or num==1):
        return 1
    else:
        print(num)
        return(num*factorial_number(num-1))
        

fact =  5
print(factorial_number(fact))
def factorial_itera(fact):
    result = 1
#now using iterative approach
    # if(fact ==0):
    #  print("1")
    while(fact>=1):
        result*= fact
        fact -= 1
    print(result)
factorial_itera(fact)
