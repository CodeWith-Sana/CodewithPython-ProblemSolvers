from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("400x500")

# Function to perform arithmetic operations
def addition():
    v1 = int(entry1.get())  # Convert input to integer
    v2 = int(entry2.get())
    ans.set(v1 + v2)  # Set the result to `ans`
    var1.set(0)  # Reset entry1 to 0
    var2.set(0)

def subtraction():
    v1 = int(entry1.get())
    v2 = int(entry2.get())
    ans.set(v1 - v2)
    var1.set(0)  # Reset entry1 to 0
    var2.set(0)

def multiplication():
    v1 = int(entry1.get())
    v2 = int(entry2.get())
    ans.set(v1 * v2)
    var1.set(0)  # Reset entry1 to 0
    var2.set(0)

def division():
    v1 = int(entry1.get())
    v2 = int(entry2.get())
    if v2 != 0:
        ans.set(v1 / v2)  # Set the result to `ans`
    else:
        ans.set("Error")  # Handle division by zero
    var1.set(0)  # Reset entry1 to 0
    var2.set(0)

# Entry fields for input
var1 = IntVar()
var2 = IntVar()
entry1 = Entry(root, textvariable=var1)
entry1.grid(row=0, column=0, padx=20, pady=10)
entry2 = Entry(root, textvariable=var2)
entry2.grid(row=0, column=1, padx=20, pady=10)

# Buttons for operations
add = Button(root, text="+", command=addition)
sub = Button(root, text="-", command=subtraction)
mul = Button(root, text="x", command=multiplication)
div = Button(root, text="/", command=division)

add.grid(row=1, column=0)
sub.grid(row=1, column=1)
mul.grid(row=2, column=0)
div.grid(row=2, column=1)

# Label to display the answer
ans = StringVar()
label = Label(root, textvariable=ans)
label.grid(row=3, column=0, padx=20, pady=20, columnspan=2)

root.mainloop()
