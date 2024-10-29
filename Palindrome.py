# name = input("enter any wod to check whether it is palindrome or not")
# #using  staright forward technique
# if(name == name[::-1]):
#     print("it is palindrome")
# else: print("not palindrome")

#s == s[::-1]
#using manual technique
s = input('enter string: ')
def palindrome(string):
    x = ""
    for i in string:
        x = i + x
        print(x)
    return x

if s == palindrome(s):
    print('its a palindrome')
else:
    print('its not a palindrome')


