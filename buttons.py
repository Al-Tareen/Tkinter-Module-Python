from tkinter import *

#Create a Window
root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a button!!")
    myLabel.pack()

#Creating a Button Widget
myButton = Button(root, text="Click Me!", padx=50, pady=50, command=myClick)
myButton.pack()

root.mainloop()
