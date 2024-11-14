from tkinter import *
from tkinter import messagebox  # Import messagebox module separately
root = Tk()
root.title("Counter Application")
root.geometry("300x450")

# Function to increment the counter
def increment_func():
    var.set(var.get() + 1)  # Get current value, increment it, and set the new value

# Function to decrement the counter
def decrement_func():
    if(var.get() == 0):
        messagebox.showerror("Error", "Counter cannot go below zero!")
        
    else:
        var.set(var.get() - 1)  # Get current value, decrement it, and set the new value
        

# Initialize the IntVar for the counter
var = IntVar(value=0)

# Label to display the counter
label = Label(root, textvariable=var, font=("Arial", 24))
label.pack(pady=20)

# Buttons to increment and decrement the counter
button1 = Button(root, text="Increment", command=increment_func)
button1.pack(padx=20, pady=10)

button2 = Button(root, text="Decrement", command=decrement_func)
button2.pack(padx=20, pady=10)

root.mainloop()
