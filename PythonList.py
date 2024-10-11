#to remove even numbers from list of integers
int_list =[]
odd_temp =[]
for i in  range(5):
    int_list.append(int(input("number plx")))  
print(int_list)
for x in int_list:
    if (x%2 == 0):
        continue
        #without remove()
    # odd_temp.append(x)  
    #using remove()
    int_list.remove(x)
print(odd_temp)
#replace the old list with new list ,  without using remove ()
# int_list = odd_temp
print(int_list)