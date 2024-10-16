#reverse a string
def reverse_string(s):
    if len(s) ==0:
        return s
    else:
        # print(s[:-1])
        return s[-1]+ reverse_string(s[:-1])
        #s[:1] means will return substring of the string that only contain the substring one char at index 1
        #s[:-1] it will return only the substring but iwthout the las one char at index n-1
print(reverse_string('hello world'))

#sum of list elements using recrusion
def sum_list(li):
    if(len(li)==0):
        return 0
    else:
        # print(li[1:])
        return li[0] + sum_list(li[1:]) 
    #li[1:] menas start with one index instead of 0
print(sum_list([12, 3, 5, 12]))
#binary seacrh using recursion
def binary_search(list , key , low , high):
    if low> high:
        return -1 
    mid  = int((low + high)/2)
    if list[mid] == key:
        return mid
    else:
        if list[mid] > key:
            return binary_search(list ,key,  low , mid-1)
        else:
            return binary_search(list , key , mid+1 , high)
arr  =[ 12, 4,  5, 6]
arr.sort()
print(arr)
print(binary_search(arr , 5, 0 , len(arr)))
    