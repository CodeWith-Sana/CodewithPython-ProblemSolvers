student_grades = {
    "Sana": 'A' ,
    "Malaika": 'B' ,
    "Usra": 'A' 
}
s_v = input("Enter the grade you want to look up: ")
search_value =  s_v.capitalize()
found_key = None
for key, value in student_grades.items():
    if value == search_value:
        found_key = key
        print(f"The student with grade {search_value} is: {found_key}")
stu_marks = {
    "sana" :[100 ,200, 300, 50],
     "malaika" : [100 ,200, 300, 50],
    "ayesha" : [100 ,200, 300, 50],
    "sana-salam" : [100 ,200, 300, 50],
}

for key , value in stu_marks.items():
    sum = 0
    for i in value:
        sum+=i
    print(f"{key} marks are :{sum}")


