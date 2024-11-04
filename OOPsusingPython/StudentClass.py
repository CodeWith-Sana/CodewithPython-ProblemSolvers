class StudentInfo:
    _name  =  ""
    _age =  None
    def __init__(self , _name , _age):
        self._name = _name
        self._age =  _age
    def displayInfo(self):
        print("Student Information")
        print(f" Student Name : {self._name}")
        print(f"Student Age :{self._age}")
class GraduatedStudent(StudentInfo):
    def __init__(self, _name , _age ,grad_year):
        super().__init__(_name, _age)
        # self._name = _name
        # self._age = _age
        self.grad_year =  grad_year
    def get_graduationYear(self):
        print("Student information")
        print(f"Student Name : {self._name}")
        print(f"Student Age : {self._age}")
        print(f"Student Graduation : {self.grad_year}")
gs1 =  GraduatedStudent("Sana" , 23 ,2024)
gs1.get_graduationYear()
# print(gs1._name)




    