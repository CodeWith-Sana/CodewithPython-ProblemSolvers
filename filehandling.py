file =  open("filename.txt" , "r")
context =  file.read()
# context =  file.readlines()
print(context)
# while context:
#     print(context)
data =  file.readline()
while data:
    print(data)
    #it is used to moved to next line
    data =  file.readline()
file =  open("filename.txt" , "a")
file.write("Hello it will be added at the end")
file =  open("filename.txt" , "r")
print(file.read())
file.close()