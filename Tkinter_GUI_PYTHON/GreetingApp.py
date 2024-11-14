from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x500")
root.title("Greeting Application")

# Entry for taking name as input from user
name = StringVar()
e1 = Entry(root, textvariable=name)
e1.pack()

def greeting():
    name1 = name.get()  # Get the name at the time of clicking the button
    messagebox.showinfo("Greeting", f"Hello {name1}, welcome to the application!")
    #exit will close the window
    exit()

# Button to trigger the greeting
b1 = Button(root, text="Click me", padx=20, pady=10, command=greeting)
b1.pack()

root.mainloop()
