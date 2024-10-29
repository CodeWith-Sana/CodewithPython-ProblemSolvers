def factorial_number(num):
    if(num<0):
        print("please input a positive number")
    else:
        if (num ==0 or num==1):
    #for + inetgars
            return 1
        else:
            return(num*factorial_number(num-1))
        

fact =  5
print(factorial_number(fact))
def factorial_itera(fact):
    result = 1
    while(fact>=1):
        result*= fact
        fact -= 1
    return result
    
print(factorial_itera(fact))
