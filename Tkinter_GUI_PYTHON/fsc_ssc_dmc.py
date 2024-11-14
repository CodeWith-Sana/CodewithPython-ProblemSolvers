from tkinter import *
from tkinter import messagebox  # Import messagebox module separately
root = Tk()
root.title("Student Dmc Application")
root.geometry("500x450")
#student class
class Student:
    def __init__(self):
        self.stud_details ={}
        self.ssc_marks  ={ "English":0 , "Urdu" : 0 , "Maths" :0 ,   "Islamyiat" : 0 , "Science": 0 , "Pakstudy" :0}  #fro ssc subjects
        self.fsc_marks  ={"English" : 0 , "Urdu" : 0 , "Physics" : 0 , "Chemistry" : 0 , "Biology" : 0 , "Islamyiat" : 0 ,}  #for fsc subjects
        self.total = 0
        self.percentage = 0
        self.grade = ''
        self.program =''
        
    def submit_details(self):
        # Check if any field is empty
        if not var1.get() or not var2.get() or not var3.get() or not var4.get() or not var5.get() or not var6.get() or not var7.get():
            # If any field is empty, show an error message
            messagebox.showerror("Input Error", "Please fill in all the fields.")
        else:
            # If all fields are filled, store the details
            self.stud_details['name'] = var1.get()
            self.stud_details['f_name'] = var2.get()
            try:
            # Attempt to convert the roll number into an integer
                roll_number = var3.get().strip()  # Get the value and strip any extra spaces
                if not roll_number.isdigit():  # Check if it's a valid number
                    raise ValueError("Please enter a valid roll number (numeric value).")
                self.stud_details['r_no'] = int(roll_number)  # Only store if valid

            except ValueError as e:
            # If the user enters a non-numeric value or invalid value
                messagebox.showerror("Invalid Input", str(e))
                return  # Exit the function to prevent storing invalid data

            self.stud_details['s/c_name'] = var4.get()
            self.stud_details['b_name'] = var5.get()
            self.stud_details['age'] = int(var6.get())
            self.stud_details['yr'] = var7.get()
            # Show success message (optional)
            messagebox.showinfo("Success", "Student details submitted successfully!")
            # print(f"Student details stored: {self.stud_details}")
            self.program  =  program_var.get()
            student_frame.pack_forget()
            if self.program == "FSC":
                fsc_frame.pack( fill="both", expand=True)
                self.marks_dict = self.fsc_marks
            else : 
                ssc_frame.pack(fill="both", expand=True)
                self.marks_dict = self.ssc_marks

    def calculate_total(self):
        
        for subject in self.marks_dict:
            self.total += self.marks_dict[subject].get()
        self.percentage  = ( self.total/600)*100
        self.percentage = (self.total / 600) * 100

        if 90 <= self.percentage <= 100:
            self.grade = "A+"
        elif 80 <= self.percentage < 90:
            self.grade = "A"
        elif 70 <= self.percentage < 80:
            self.grade = "B"
        elif 60 <= self.percentage < 70:
            self.grade = "C"
        elif 50 <= self.percentage < 60:
            self.grade = "D"
        elif 40 <= self.percentage < 50:
            self.grade = "E"
        else:
            self.grade = "Fail"


                
            
    def validate_marks(self):
    # Loop through each subject and its corresponding IntVar in the dictionary
        for subject, var in self.marks_dict.items():
            mark = var.get()  # Get the entered mark for the subject
            if mark == 0:  # Check if the mark is 0, which can indicate an empty field
                messagebox.showerror("Input Error", f"Please enter the mark for {subject}.")
                return False 
            
            if mark <0 or mark >100:
                messagebox.showerror("Input Error", f"Mark for {subject} must be between 0 and 100.")
                return False  # Return False if there's an error
            # Show an error message if the mark is out of range
              
    
    # If all marks are valid
        return True

# Function to save the marks
    def save_marks(self):
        if self.validate_marks():
        # Proceed to save 
            messagebox.showinfo("Success", "Marks saved successfully!")
        
        
    def save_certificate(self):
        # Generate the certificate details as text
        certificate_text  = f"Certificate for {self.stud_details['name']}\n"
        certificate_text += f"Father's Name: {self.stud_details['f_name']}\n"
        certificate_text += f"Roll Number: {self.stud_details['r_no']}\n"
        certificate_text += f"Board Name: {self.stud_details['b_name']}\n"
        certificate_text += f"School/College Name: {self.stud_details['s/c_name']}\n"
        certificate_text += "\nSubject-wise Marks:\n"
        certificate_text += f"{'Subject':<20}{'Obtained Marks':<15}{'Total Marks':<15}\n"
    
        for subject, marks in self.ssc_marks.items():
            certificate_text += f"{subject:<20}{marks.get():<15}{100:<15}\n"
    
        certificate_text += "\nTotal Marks: 600\n"
        certificate_text += f"Obtained Marks: {self.total}\n"
        certificate_text += f"Percentage: {self.percentage:.2f}%\n"
        certificate_text += f"Grade: {self.grade}\n"
    
    # Save the text to a file
        file_name  = f"{self.stud_details['r_no']}.txt"
        with open(file_name, "w") as file:
            file.write(certificate_text)
    
    # Show success message
        messagebox.showinfo("Success", "Certificate saved successfully!")
        exit()
    def program_subject(self):
        pass

    def generate_certificate(self):
        self.calculate_total()
        certificate_window = Toplevel(root)  # Creating a new window
        certificate_window.title("Certificate")
        certificate_window.geometry("800x800")
        # Create a canvas for custom drawing
        canvas = Canvas(certificate_window, width=600, height=600)
        canvas.pack()
        # Draw certificate border
        canvas.create_text(300 , 40 , text = self.stud_details['b_name'] , font=("Helvetica", 16, "bold"))
        # Add student details
        canvas.create_text(120, 80, text=f" Student Name: {self.stud_details['name']}", font=("Helvetica", 12))
        canvas.create_text(120, 100, text=f" Father's Name: {self.stud_details['f_name']}", font=("Helvetica", 12))
        canvas.create_text(120, 120, text=f"Roll Number: {self.stud_details['r_no']}", font=("Helvetica", 12))
        y_pos = 170  # Initial vertical position for the table

        # Table Header
        canvas.create_text(100, y_pos, text="Subject", font=("Helvetica", 12, "bold"))
        canvas.create_text(300, y_pos, text="Obtained Marks", font=("Helvetica", 12, "bold"))
        canvas.create_text(500, y_pos, text="Total Marks", font=("Helvetica", 12, "bold"))
        
        y_pos += 30  # Move down after the header
        
        
        # Subjects and their marks
        for subject, marks in self.marks_dict.items():
            print(subject, marks.get())
            canvas.create_text(100, y_pos, text=subject, font=("Helvetica", 10))
            canvas.create_text(300, y_pos, text= marks.get(), font=("Helvetica", 10))
            canvas.create_text(500, y_pos, text="100", font=("Helvetica", 10))  # Total marks per subject
            y_pos += 30  # Move down for the next row
        
        # Display Total Marks, Percentage, and Grade at the bottom
        canvas.create_text(100, y_pos, text="Total Marks : 600", font=("Helvetica", 12, "bold"))
        canvas.create_text(300, y_pos, text= f"Obtained Marks {self.total}", font=("Helvetica", 12))
        y_pos += 30
        
        canvas.create_text(100, y_pos, text="Percentage", font=("Helvetica", 12, "bold"))
        canvas.create_text(300, y_pos, text=f"{self.percentage:.2f}%", font=("Helvetica", 12))
        y_pos += 30
        
        canvas.create_text(100, y_pos, text="Grade", font=("Helvetica", 12, "bold"))
        canvas.create_text(300, y_pos, text=self.grade, font=("Helvetica", 12))
        save_button = Button(certificate_window, text="Save Certificate", command=self.save_certificate)
        save_button.pack(pady=10)
        
    

student  =Student()   
# Creating a Frame container inside the root window
student_frame = Frame(root)
# creating label for student 

l2 = Label(student_frame , text="Please Enter Student Details..." ,font=("Helvetica", 10, "bold"))

l2.grid(row  =0 , column  = 0 , padx = 2 , pady = 10)
# Label and entry for student name
l3 = Label(student_frame, text="Student Name" ,font =("Helvectica",8 ,"bold"))
l3.grid(row=2, column=0, padx=20, pady=5 )

var1 = StringVar()
e1 = Entry(student_frame, textvariable=var1)
e1.grid(row=2, column=1, padx=10, pady=5 , )
#label and entry father name
l4 = Label(student_frame, text="Father Name" ,font =("Helvectica",8 ,"bold"))
l4.grid(row=3, column=0, padx=10, pady=5)

var2 = StringVar()
e2 = Entry(student_frame, textvariable=var2)
e2.grid(row=3, column=1, padx=10, pady=5)
#label and entry for roll number
l5  =  Label(student_frame, text= "Roll number" ,font =("Helvectica",8 ,"bold"))
l5.grid(row=4, column=0, padx=10, pady = 5)
var3 = StringVar()
e3 = Entry(student_frame , textvariable= var3)
e3.grid(row=4, column=1, padx=10, pady =5)
#creating label and entry for institue name
l6 = Label(student_frame , text ="School/College Name " ,font =("Helvectica",8 ,"bold"))
l6.grid(row=5, column=0, padx=10 , pady  =5)
var4 =  StringVar()
e4 =Entry(student_frame , textvariable= var4 )
e4.grid(row = 5 , column= 1 , padx=10 , pady= 5)

#creating label and entry for BOARD name
l7 = Label(student_frame , text= "Board Name " ,font =("Helvectica",8 ,"bold"))
l7.grid(row = 6 , column = 0 , padx=10 , pady =5)
var5 = StringVar()
e5  =Entry(student_frame ,textvariable= var5)
e5.grid(row = 6 , column = 1 , padx=10 , pady =  5)
#creating label and entry for age 
l8  = Label(student_frame ,text= "Age" ,font =("Helvectica",8 ,"bold"))
l8.grid(row = 7 , column = 0, padx=10 , pady =  5)
var6 = StringVar()
e6 = Entry(student_frame ,textvariable= var6)
e6.grid(row = 7 , column = 1, padx=10, pady =5)
#creating label and entry for year of passing
l9 = Label(student_frame ,text ="Year of Passing" ,font =("Helvectica",8 ,"bold"))
l9.grid(row = 8 , column = 0, padx=10, pady= 5)
var7 = StringVar()
e7  =Entry(student_frame ,textvariable= var7)
e7.grid(row = 8 , column = 1 , padx = 10, pady= 5)
#radio button to check if student is ssc or fsc 
# Set the default program to "SSC" or "FSC"
program_var = StringVar()
program_var.set("SSC")  # Set default value to "SSC"
p_ssc = Radiobutton(student_frame , text = "SSC" ,variable=program_var, value= "SSC" )
p_fsc = Radiobutton(student_frame , text = "FSC"  ,variable=program_var, value= "FSC")
p_ssc.grid(row= 9 , column =0 , padx =5 , pady = 5)
p_fsc.grid(row= 9 , column =1 , padx =5 , pady = 5)


#adding frame to the parent window
# button for to submit details about student
b1 =  Button(student_frame ,text ="Submit", command = student.submit_details ,padx = 15,)
b1.grid(row= 20 , column= 0 ,  pady = 20)

student_frame.pack()
#creating FSc Frame
fsc_frame = Frame(root)
# creating label for FSC subjects with entry for marks

f_label = Label(fsc_frame , text  ="Please Enter Marks corresponding to specific subject.... \n ( note (in range 0-100))" , font=("Helvectica" , 10 , "bold"))
f_label.grid(row = 0 , column= 0 , padx = 10 ,pady =5)

row1 = 2  # Start from row 2 for labels and entries
for subject, mark in student.fsc_marks.items():
        
    l = Label(fsc_frame, text=subject, font=("Helvetica", 10, "bold"))
    l.grid(row=row1, column=0, padx=10, pady=5)
    
    var = IntVar()  # Create a new IntVar for each subject
    entry = Entry(fsc_frame, textvariable=var)
    entry.grid(row=row1, column=1, padx=10, pady=5)
    student.fsc_marks[subject] = var
    row1 += 1  # Move to the next row for the next subject
save_button = Button(fsc_frame, text  ="Save" , padx = 15 , command = student.save_marks)
cert_btn = Button(fsc_frame, text = "Get Certificate" , padx = 15 ,command = student.generate_certificate)
save_button.grid(row = row1 , column= 0 ,pady = 20 )
cert_btn.grid(row = row1 , column= 1 ,pady = 20 )
#creating ssc_frame
ssc_frame  = Frame(root)
s_label =  Label(ssc_frame  , text= "Please Enter Marks corresponding to specific subject.... \n (note(in range 0-100))" , font=("Helvectica" , 10 , "bold"))
s_label.grid(row = 0 , column= 0 , padx = 10 , pady = 5)
row = 1  # Start from row 1 for labels and entries
for subject, mark in student.ssc_marks.items():
    l = Label(ssc_frame, text=subject, font=("Helvetica", 10, "bold"))
    l.grid(row=row, column=0, padx=10, pady=5)
    
    var = IntVar()  # Create a new IntVar for each subject
    entry = Entry(ssc_frame, textvariable=var)
    entry.grid(row=row, column=1, padx=10, pady=5)
    student.ssc_marks[subject] = var
    row += 1  # Move to the next row for the next subject
s_button = Button(ssc_frame, text  ="Save" , padx = 15 , command = student.save_marks)
g_btn = Button(ssc_frame, text = "Get Certificate" , padx = 15 ,command = student.generate_certificate)

s_button.grid(row = row , column = 0 , pady = 20)
g_btn.grid(row = row, column  = 1, pady=20)





root.mainloop()