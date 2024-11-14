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
    #func to calculate total
    def calculate_marks(self, marks):
        if marks is None:
            marks = {}
        total = sum(marks.values())
        return total
    #func to calculate percentage
    def percent_calculate(self, total):
        percentage = (total / 600) * 100
        return percentage
    #func to calculate grades
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
    #to generate certificate in console
    def generate_certificate(self, marks, total, percent, grade):
        
        print(f"                      {self.stud_details.get('b_name') :<100}                 ")
        print(f"                 {self.stud_details.get('s/cname')}               ")
        print(f"                 Passing year: {self.stud_details.get('yr')}               ")
        print('_' * 100)
        print(f"Roll No {self.stud_details.get('rollno')}")
        print(f"Student Name {self.stud_details.get('s_name')}")
        print(f"Father Name {self.stud_details.get('f_name')}")
        print("-" * 100)
        print(f"    Subject            Total Marks     Obtained Marks")
        for subject, value in marks.items():
            print(f"    {subject:<20}|     100 |   {value:<20}|")
        print(f"    Total Marks:    600 |    Obtained Marks:  {total} |    Grade: {grade}")
        #to save as txt file
        file_name = f"certificate_{self.stud_details.get('rollno')}.txt"
        # Open a file in write mode, and write the certificate text to the file.
        # The file will be closed automatically when the block of code is exited.
        # The 'with' statement ensures that the file is automatically closed after writing.
        with open(file_name, "w") as file :
            file.write(f"                      {self.stud_details.get('b_name') :<100}                 \n")
            file.write(f"                 {self.stud_details.get('s/cname')}               \n")
            file.write(f"                 Passing year: {self.stud_details.get('yr')}               \n")
            file.write('_' * 100 + "\n")
            file.write(f"Roll No {self.stud_details.get('rollno')}\n")
            file.write(f"Student Name {self.stud_details.get('s_name')}\n")
            file.write(f"Father Name {self.stud_details.get('f_name')}\n")
            file.write("-" * 100 + "\n")
            file.write(f"    Subject            Total Marks     Obtained Marks\n")
            for subject, value in marks.items():
                file.write(f"    {subject:<20}|     100 |   {value:<20}|\n")
            file.write(f"    Total Marks:    600 |    Obtained Marks:  {total} |    Grade: {grade}\n")
            
            
            file.close()
            print("Certificate has been saved successfully...")
            
        

class FSC(Student):
    def __init__(self):
        super().__init__()
        self.subject_marks = {}
        self.sub_by_program = {
            'computer science': ["Programming", "Mathematics", "English", "Physics", "Chemistry", "Islamic Studies"],
            "pre-medical": ["Biology", "Chemistry", "Physics", "English", "Urdu", "Islamic Studies"]
        }
    #func to ask user to enter program name 
    def get_program(self):
        while True:  # Start an infinite loop to continuously ask until valid input is received
            program = input("Are you a Computer Science or Pre-Medical student? ").strip().lower()
            if program in self.sub_by_program:
                return self.sub_by_program[program]
            else:
                print("Invalid input. Please enter 'Computer Science' or 'Pre-Medical'.")
                
    #func to allow user to enter marks for the Fsc subjects
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
        


class SSC(Student):
    def __init__(self):
        super().__init__()
        self.ssc_marks = {}
  #func to allow users to enters marks for SSC subjects
    def get_ssc_marks(self):
        subjects = ['English', 'Urdu', 'Maths', 'Islamyat', 'Pakstudy', 'Science']
        print("Please enter marks for at least 6 subjects (0-100):")
        for subject in subjects:
            while True:
                try:
                    mark = int(input(f"Enter Mark for {subject}: "))
                    if 0 <= mark <= 100:
                        self.ssc_marks[subject] = mark
                        break
                    else:
                        print("Mark must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
#craeting object for Fsc class and SSc class
fsc = FSC()

#input details for Fsc student
# fsc.input_student_details()
# fsc.get_subject_marks()
# sum =  fsc.calculate_marks(fsc.subject_marks)
# per  =fsc.percent_calculate(sum)
# g = fsc.get_grades(per)
# fsc.generate_certificate(fsc.subject_marks, sum , per , g)
#for ssc 

ssc = SSC()

#input details for SSC student
ssc.input_student_details()
ssc.get_ssc_marks()

sum =  ssc.calculate_marks(ssc.ssc_marks)

per  = ssc.percent_calculate(sum)

g = ssc.get_grades(per)

ssc.generate_certificate(ssc.ssc_marks, sum , per , g)

