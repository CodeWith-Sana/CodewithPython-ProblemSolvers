import math  

# Function to compute LCM  
def lcm(x, y):  
    return abs(x * y) // math.gcd(x, y)  

# Function to compute HCF (GCD)  
def hcf(x, y):  
    return math.gcd(x, y)  

# Example usage  
num1 = 12  
num2 = 15  

print("HCF (GCD) of", num1, "and", num2, "is:", hcf(num1, num2))  # Output: 3  
print("LCM of", num1, "and", num2, "is:", lcm(num1, num2))        # Output: 60