from tkinter import *

#Create a Window
root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your Name: ")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

#Creating a Button Widget
myButton = Button(root, text="Enter your Name!", padx=50, pady=50, command=myClick)
myButton.pack()

root.mainloop()
