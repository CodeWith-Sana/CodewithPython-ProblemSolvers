import tkinter as tk
from tkinter import messagebox


class Student:
    def __init__(self):
        self.stud_details = {}

    def input_student_details(self, s_name, f_name, rollno, cname, bname, age, gender, year):
        self.stud_details['s_name'] = s_name
        self.stud_details['f_name'] = f_name
        self.stud_details['rollno'] = rollno
        self.stud_details['s/cname'] = cname
        self.stud_details['b_name'] = bname
        self.stud_details['age'] = age
        self.stud_details['g'] = gender
        self.stud_details['yr'] = year

    def calculate_marks(self, marks):
        return sum(marks.values())

    def percent_calculate(self, total):
        return (total / 600) * 100

    def get_grades(self, percent):
        if 90 <= percent <= 100:
            return "A+"
        elif 80 <= percent < 90:
            return "A"
        elif 70 <= percent < 80:
            return "B"
        elif 60 <= percent < 70:
            return "C"
        elif 50 <= percent < 60:
            return "D"
        elif 40 <= percent < 50:
            return "E"
        else:
            return "F"  # Fail if below 40

    def generate_certificate(self, marks, total, percent, grade):
        certificate_text = f"""
                      {self.stud_details.get('b_name') :<100}                 
                 {self.stud_details.get('s/cname')}               
                 Passing year: {self.stud_details.get('yr')}               
{'_'* 100}
Roll No {self.stud_details.get('rollno')}
Student Name {self.stud_details.get('s_name')}
Father Name {self.stud_details.get('f_name')}
{'-'*100}
    Subject            Total Marks     Obtained Marks"""
        
        for subject, value in marks.items():
            certificate_text += f"\n    {subject:<20}|     100 |   {value:<20}|"
        
        certificate_text += f"\n    Total Marks:    600 |    Obtained Marks:  {total} |    Grade: {grade}"

        # Create a file name based on the student's roll number
        file_name = f"Certificate_{self.stud_details.get('rollno')}.txt"

        # Save the certificate to a text file
        with open(file_name, 'w') as file:
            file.write(certificate_text)
        
        return file_name


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Certificate Generator")
        self.geometry("400x500")
        self.student = Student()
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entries for student details
        self.s_name_label = tk.Label(self, text="Student Name")
        self.s_name_label.pack()
        self.s_name_entry = tk.Entry(self)
        self.s_name_entry.pack()

        self.f_name_label = tk.Label(self, text="Father Name")
        self.f_name_label.pack()
        self.f_name_entry = tk.Entry(self)
        self.f_name_entry.pack()

        self.rollno_label = tk.Label(self, text="Roll Number")
        self.rollno_label.pack()
        self.rollno_entry = tk.Entry(self)
        self.rollno_entry.pack()

        self.cname_label = tk.Label(self, text="College Name")
        self.cname_label.pack()
        self.cname_entry = tk.Entry(self)
        self.cname_entry.pack()

        self.bname_label = tk.Label(self, text="Board Name")
        self.bname_label.pack()
        self.bname_entry = tk.Entry(self)
        self.bname_entry.pack()

        self.age_label = tk.Label(self, text="Age")
        self.age_label.pack()
        self.age_entry = tk.Entry(self)
        self.age_entry.pack()

        self.gender_label = tk.Label(self, text="Gender")
        self.gender_label.pack()
        self.gender_entry = tk.Entry(self)
        self.gender_entry.pack()

        self.year_label = tk.Label(self, text="Year of Passing")
        self.year_label.pack()
        self.year_entry = tk.Entry(self)
        self.year_entry.pack()

        # Subject Marks Entry
        self.marks_label = tk.Label(self, text="Enter Marks for Subjects (separated by commas)")
        self.marks_label.pack()
        self.marks_entry = tk.Entry(self)
        self.marks_entry.pack()

        # Submit button to generate certificate
        self.submit_button = tk.Button(self, text="Generate Certificate", command=self.generate_certificate)
        self.submit_button.pack()

    def generate_certificate(self):
        # Getting all the inputs
        s_name = self.s_name_entry.get()
        f_name = self.f_name_entry.get()
        rollno = self.rollno_entry.get()
        cname = self.cname_entry.get()
        bname = self.bname_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        year = self.year_entry.get()

        # Marks as a dictionary (simple example)
        marks_input = self.marks_entry.get().split(',')
        marks = {f"Subject {i+1}": int(mark.strip()) for i, mark in enumerate(marks_input)}

        # Fill student details
        self.student.input_student_details(s_name, f_name, rollno, cname, bname, age, gender, year)

        # Calculate total, percentage, and grade
        total = self.student.calculate_marks(marks)
        percent = self.student.percent_calculate(total)
        grade = self.student.get_grades(percent)

        # Generate and save certificate
        file_name = self.student.generate_certificate(marks, total, percent, grade)
        messagebox.showinfo("Success", f"Certificate generated and saved as {file_name}")


if __name__ == "__main__":
    app = GUI()
    app.mainloop()
