
var1 = 'home'
var2 = 'welcome'
print("before swap variables" , var1 , var2)

# swapping using temp variable
temp = var1
var1 =  var2
var2 = temp
print("after swap variables" , var1 , var2)

#swapping without temp variable
a  = 12
b = 15
print("before swap variables" , a , b)
# a=a+b    
# b=a-b    
# a=a-b  
a,b = b,a