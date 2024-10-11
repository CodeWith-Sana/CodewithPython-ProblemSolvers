user_input = input("enter any sentence")
char_freq = {}
for x in user_input:
    if x in char_freq:
        char_freq[x] +=1
    else:
        char_freq[x] =1
for char , count in char_freq.items():  
    print(f"Character: {char}, Frequency: {count}")
