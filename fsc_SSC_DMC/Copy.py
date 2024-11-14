class Student:
    def __init__(self):
        self.stud_details = {}

    def input_student_details(self):
        print("Enter details")
        self.stud_details['s_name'] = input("Enter name: ")
        self.stud_details['f_name'] = input("Enter father name: ")
        self.stud_details['rollno'] = input("Enter rollno: ")
        self.stud_details['s/cname'] = input("Enter school/college name: ")
        self.stud_details['b_name'] = input("Enter board name: ")
        self.stud_details['age'] = input("Enter age: ")
        self.stud_details['g'] = input("Enter gender: ")
        self.stud_details['yr'] = input("Enter year of passing: ")

    def calculate_marks(self, marks=None):
        if marks is None:
            marks = {}
        total = sum(marks.values())
        return total

    def percent_calculate(self, total):
        percentage = (total / 600) * 100
        return percentage

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
        
        print(f"Certificate saved as {file_name}")

class FSC(Student):
    def __init__(self):
        super().__init__()
        self.subject_marks = {}
        self.sub_by_program = {
            'computer science': ["Programming", "Mathematics", "English", "Physics", "Chemistry", "Islamic Studies"],
            "pre-medical": ["Biology", "Chemistry", "Physics", "English", "Urdu", "Islamic Studies"]
        }

    def get_program(self):
        while True:
            try:
                program = input("Are you a Computer Science or Pre-Medical student? ").strip().lower()
                if program in self.sub_by_program:
                    return self.sub_by_program[program]
                    break
                else:
                    print("Invalid input. Please enter 'Computer Science' or 'Pre-Medical'.")
            except SyntaxError:
                print("Incorrect spelling")  

    def get_subject_marks(self):
        subjects = self.get_program()
        print("Please enter marks for at least 6 subjects (0-100):")
        for subject in subjects:
            while True:
                try:
                    mark = int(input(f"Enter Mark for {subject}: "))
                    if 0 <= mark <= 100:
                        self.subject_marks[subject] = mark
                        break
                    else:
                        print("Mark must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")       

# Example Usage
fsc_student = FSC()
fsc_student.input_student_details()
fsc_student.get_subject_marks()
marks = fsc_student.subject_marks
total = fsc_student.calculate_marks(marks)
percent = fsc_student.percent_calculate(total)
grade = fsc_student.get_grades(percent)
fsc_student.generate_certificate(marks, total, percent, grade)

