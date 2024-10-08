def Even_ODD(num):
    """
    This function checks if a given number is even or odd."""
    if(num%2 ==0):
        return True
    else:
        return False
var = Even_ODD(12)
if(var != False):
    print("the in input number is even")
else:
    print("the number is odd")
