# class demo:
#     name = "Sana"
#     age = 10
#     x = 'apple'
# obj1 = demo()
# obj2 =  demo()
# #using hasattr 

# print(hasattr(obj1,'y'))
# #setattr
# setattr(obj1 ,'age' , 20)
# print(obj1.age)
# print(obj2.age)
# setattr(obj2 ,'y' , 'sana')
# print(obj2.y)
# # print(obj1.y)
# # print(obj1.y) gives an error
# #using delattr
# # delattr(obj1 , 'x')
# # print(vars(obj1))
# print(hasattr(obj2,'x'))
# print(obj2.x)
# delattr(obj2 ,'x')
# # print(dir(obj2))
# # print(dir(obj1))

class demo:
    name = "Sana"
    age = 10
    x = 'apple'

obj1 = demo()
obj2 = demo()
print(obj2.x)
# Set 'x' explicitly on obj2 as an instance attribute
setattr(obj2, 'x', 'mango')
print(obj2.x)
print(obj2.__dict__)
#AttributeError: 'demo' object has no attribute 'x' (without) updating the value)
delattr(obj2, 'x')
print(hasattr(obj2, 'x'))  
print(obj2.x)
print(obj2.__dict__)  
print(demo.__dict__)
'''to delete the class attribute for all objects'''
# del demo.x
# print(hasattr(obj1, 'x'))  
# print(hasattr(obj2, 'x'))
'''delattr(Demo, 'x')   Deletes the class attribute `x` from Demo
print(hasattr(obj, 'x')) '''
setattr(obj1 , 'marks' , 200)
print(obj1.marks)
print(obj1.__dict__)