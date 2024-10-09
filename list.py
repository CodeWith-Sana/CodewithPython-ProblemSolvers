name_list = ["sana" , "kashmala", "malaika" , "nida"]
for item in name_list:
    print("name is" , item)
print(name_list)

#creating tuple
fruits = ("apple" , 100 , "mango")
print(fruits)  

#creating set
grocery = ("milk" , "vegetables" , "water")
print(grocery)
# grocery.remove("milk") will gives an error because of imutable
print(grocery)
#set {} , list [] , tuple()
#creating dictionary
student_record = {
    "name":"Sana",
    "id":"216102" 
}
print(student_record.get("name"))
print(student_record.keys())
student_record["age"] = 20
print(student_record.values())
print(student_record)


