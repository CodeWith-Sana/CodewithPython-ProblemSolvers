class Employee:
    __name  = ""
    __salary  = None
    def __init__(self , name):
        self.__name =  name
    def setSalary(self ,salary):
        
        self.__salary = salary
    def getSalary(self):
        print(f"Name is {self.__name}")
        print(f"Salary : {self.__salary}")
e =  Employee("Malaika Khan")
e.setSalary(2000.0)
e.getSalary()
# print(e.__name)


