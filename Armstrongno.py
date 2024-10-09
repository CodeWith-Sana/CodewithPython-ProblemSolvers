def armStrong(n):
    count = 0 
    d_list = []
    value = 0
    for digit in str(n):
         d_list.append(int(digit)) 
         count += 1 
    for digit in d_list:
        value += digit ** count
    if value == n:
        print(f"{n} is an Armstrong number.")
    else:
        print(f"{n} is not an Armstrong number. {value}")


armStrong(20)
        