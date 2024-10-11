#to print sudent with highest grades
student = {
    "Sana":'A',
    "Malaika": 'B',
    "Usra": 'D'
}
student["ALi"] = 'B'
student["Ali Khan"] = 'A+'
student["Marwa"] = 'A'
for key in student:
    if student[key]== 'A' or student[key]=='A+':
        print(f"{key} has grade of {student[key]}")
    