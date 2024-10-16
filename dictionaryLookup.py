student_grades = {
    "Sana": 'A' ,
    "Malaika": 'B' ,
    "Usra": 'D' 
}
s_v = input("Enter the grade you want to look up: ")
search_value =  s_v.capitalize()
found_key = None
for key, value in student_grades.items():
    if value == search_value:
        found_key = key
        break
if found_key:
    print(f"The student with grade {search_value} is: {found_key}")
else:
    print("No student found with that grade.")
