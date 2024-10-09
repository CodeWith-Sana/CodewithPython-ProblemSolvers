#to solve quadratic equation
# ax^2 + bx + c
import math  
# Function to solve the quadratic equation  
def solve_quadratic(a, b, c):  
    # Calculate the discriminant  
    d = (b**2) - (4*a*c)  
    
   
    sol1 = (-b + math.sqrt(d)) / (2 * a)  
    sol2 = (-b - math.sqrt(d)) / (2 * a)  
    
    return sol1, sol2  

 
a = 1  
b = 5  
c = 6  
solution = solve_quadratic(a, b, c)  
print("The solutions are:", solution)