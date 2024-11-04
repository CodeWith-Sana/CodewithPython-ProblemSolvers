'''class student:
    def __init__(self , name):
        self.name =  name         #create only instance attribute not class for each instance
s1 =  student("Sana")
print(s1.name)
print(s1.__dict__)
#override the instace attribute b/c name is created in init 
setattr(s1 , 'name' , 'Malaika')
print(s1.name)
print(s1.__dict__)
'''
# class student:
#     # Class attribute declared without an initial value
#     name = None  
#     # def __init__(self , name):
#     #     self.name = name
# s1 = student()
# print(hasattr(s1 , 'name'))
# # s1 =  student("Khan")
# print(s1.name)
# print(s1.__dict__)

class Demo:
    class_attribute = "This is a class attribute"  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute

# Create an instance of Demo
obj = Demo("Alice")

# Check for attributes
print(hasattr(obj, 'name'))           # True (instance attribute)
print(hasattr(obj, 'class_attribute')) # True (class attribute)
print(getattr(obj , 'name' ))
setattr(obj , 'name' , "Sara")
print(getattr(obj , 'name' ))
# Now delete the instance attribute
delattr(obj, 'name')

# Check again
print(hasattr(obj, 'name'))           # False (instance attribute deleted)
print(hasattr(obj, 'class_attribute')) # True (class attribute still exists)
obj.class_attribute = "sana"
delattr(obj , 'class_attribute')
print(hasattr(obj , 'class_attribute'))
# print(Demo.name)   #erroo type object 'Demo' has no attribute 'name'


