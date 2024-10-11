# #take sentence as input and split into words store in set.
# sentence = """Hello i am sana . Sana is sana , hello , Hello"""
# word_list = []
# #using split method
# word_list.append(sentence.split())
# print(word_list)
# #without Split()
# for x in sentence:
#     if x =="":
#         word_list.append(x)
# print(word_list)
# #to check unique_words in the word_list
# uniq_words = []
# count = 0
# for x in range(len(word_list)):
#     if word_list[x]  in uniq_words:
#         continue
#     uniq_words.append(word_list[x])
#     count +=1
# print(f"the unique words in sentence are {uniq_words} and their count is {count}")
sentence = """Hello i am sana. Sana is sana, hello, Hello"""

# Step 1: Convert the sentence to lowercase and split into words
words = sentence.lower().replace(",", "").replace(".", "").split()

# Step 2: Store the words in a set to get unique words
unique_words = set(words)
# Step 3: Count the unique words
unique_count = len(unique_words)

# Step 4: Output the result
print(f"The unique words in the sentence are: {unique_words}")
print(f"The count of unique words is: {unique_count}")
