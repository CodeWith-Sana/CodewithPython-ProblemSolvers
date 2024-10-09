word = input("enter any word")
#to count number of vowels in string
count =0

for i in word:
    if(i =='a' or i=='i'  or  i=='o'  or  i=='e' or i =='u'):
        count +=1
print(f"number of vowels in the input string are:{count}")        