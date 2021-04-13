from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Learn to Code at Codemy.com")
root.iconbitmap('C:/Users/User/Desktop/CAMEO_Register/CAMEO_Register/favicon.ico')

#r = IntVar()
#r.set("2")

TOPPINGS = [
	("Pepperoni", "Pepperoni"),
	("Cheese", "Cheese"),
	("Mushrooms", "Mushrooms"),
	("Onion", "Onion"),
]

pizza = StringVar()
#pizza.set("Choose your toppings")

for text, topping in TOPPINGS:
	Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

def clicked(value):
	myLabel = Label(root, text=value)
	myLabel.pack()

#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

#myLabel = Label(root, text=pizza.get())
#yLabel.pack()

myButton = Button(root, text="Add Toppings", command=lambda: clicked(pizza.get()))
myButton.pack()
root.mainloop()
