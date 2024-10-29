
def list_array(li):
    if len(li) ==0:
        return True
    else:
        f_type =  type(li[0])
        new_list = []  # Create a new list to store elements of the same type
        for i in li:
            if type(i) == f_type:
                new_list.append(i) 
                 # Add the element to the new list if it matches the type
               
        return new_list
array = list_array([2 , 4, 6 ,'i' ,'hello' ,2.0])

print(array)
# print(locals())
print(f"locals {locals()}")
print(f"globalss {globals()}")
# print(globals())




