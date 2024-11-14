#to implement single inheritance in pyhton
class Employee:
    def __init__(self , name , age , salary):
        self.name = name
        self.age = age
        self.salary = salary
class Manager(Employee):
    def __init__(self, name, age, salary , department):
        super().__init__(name, age, salary)
        self.department =  department
    def display_info(self):
        print("Employee Details")
        print(f"Employee Name : {self.name}")
        print(f"Employee Age : {self.age}")
        print(f"Employee Salary : {self.salary}")
        print(f"Employee Department : {self.department}")
m1 =  Manager("Malaika Khan" ,23 , 500000 , "HR department")
m1.display_info()