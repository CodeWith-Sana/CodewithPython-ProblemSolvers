def Fibnocci_seq(n):
    fib = [0, 1]  # Initialize the list with the first two Fibonacci numbers
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2]) 
         # Use append to add the next Fibonacci number
    return fib

seq = Fibnocci_seq(20)
print(seq)
for i in range(11 , 20):
    pass
    # Print numbers in the range 11 to 20 only
for num in (seq):
    if num >= 11 and num <= 20:
        print(num)
