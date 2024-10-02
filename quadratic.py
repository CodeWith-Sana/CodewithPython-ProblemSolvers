#to solve quadratic equation
# ax^2 + bx + c
import cmath  
# Function to solve the quadratic equation  
def solve_quadratic(a, b, c):  
    # Calculate the discriminant  
    d = (b**2) - (4*a*c)  
    
    # Find two solutions  
    sol1 = (-b + cmath.sqrt(d)) / (2 * a)  
    sol2 = (-b - cmath.sqrt(d)) / (2 * a)  
    
    return sol1, sol2  

# Example usage  
a = 1  
b = 5  
c = 6  
solution = solve_quadratic(a, b, c)  
print("The solutions are:", solution)