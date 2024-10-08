import math
def is_prime(n):
    if n <= 1:
        return False  
    # 0 and 1 are not prime numbers
    for i in range(2, int(math.sqrt(n)) + 1): 
        if n % i == 0:
            return False 
         # n is divisible by i, so it's not prime
    return True

#to check prime numbers in interval 1-10
for i in range(1, 10):
    abc = is_prime(i)
    if(abc ==True):
        print(i , " is prime")

   