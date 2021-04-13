from tkinter import *

#Create a Window
root = Tk()

#Creating a Label Widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Al Tareen")

#Shoving widget onto screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)

#Running continuous loop for mouse-purposes
root.mainloop()
