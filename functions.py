def my_function(*args):
#*args is used whn dont know the number of arguments to pass in advanced
    for i in  args:
        print(f"hello! i am {i}")
my_function("sana" , "Malaika" , "sara")
def my_func(**args):
    #it is used whn dont know the number of keyword to pass in advance
    print(f"his last name is {args["l_name"]}")
my_func(f_name  = "Sana" , l_name = " khan")
#example fro this 
def order_system(name , *items , **payop):
    print(f" Customer name is : {name}  have order items : {items} and have given payment option {payop.values()}")
order_system("Sana" ,[1, 2, 3, 5,6] , key = "Advacnce payment" )
