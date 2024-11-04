class Student:
   def __init__(self, name, age):
      self.name = name
      self.age = age
    
   def display(self):
      print("Name:", self.name)
      print("Age:", self.age)

s = Student("John", 20)
s.display()
