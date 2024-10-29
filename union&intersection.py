set1 = set((12, 3, 5 , 100 , 101 , 11 , 12))
set2 = set((12, 5, 3 , 2 ,1))
#union of two sets
u_set = set()
for x in (set1):
    if(x not in u_set):
        u_set.add(x)
for y in set2:
    if(y not in u_set):
        u_set.add(y)
print(u_set)
intsect_set = set()
def intersection(set1 , set2):
    for x in set1:
        if(x in set2):
            intsect_set.add(x)
        
    print(intsect_set)
intersection(set1 , set2)
# as set doesnot accept duplicate values it will be eliminated.
print(set1)


