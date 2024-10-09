element = [1, 3, 1, 5, 12, 3, 1, 6]
print("Original List:", element)

unique_elements = []
for i in element:
    if i not in unique_elements:
          # Only add if it's not already in unique_elements
        unique_elements.append(i)

print("List with duplicates removed:", unique_elements)
#using set 
uniq_set =  set(element)
print(uniq_set)

        
         


