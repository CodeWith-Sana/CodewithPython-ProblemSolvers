def Fibnocci_seq(n):
    fib = [0, 1]  # Initialize the list with the first two Fibonacci numbers
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2]) 
         # Use append to add the next Fibonacci number
    print(fib)

Fibnocci_seq(10)

