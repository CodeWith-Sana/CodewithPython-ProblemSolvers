def Calculator_func(num1  = 0 , num2= 0 , op = '+'):
    if op == '+':
        return num1+ num2
    elif op == '-':
        return num1-num2
    elif op =='/':
        return num1/num2
    elif op =='*':
        return num1*num2
    
result = Calculator_func(1.4,12 , '+' )
if(result == None):
    print("wrong data given")
else: print(result)
