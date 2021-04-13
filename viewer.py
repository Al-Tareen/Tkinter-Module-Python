from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Learn to Code at Codemy.com")
root.iconbitmap('C:/Users/User/Desktop/CAMEO_Register/CAMEO_Register/favicon.ico')

my_img1 = ImageTk.PhotoImage(Image.open("images/1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/3.jpeg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/4.jpeg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/5.jpeg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
	global my_label
	global button_forward
	global button_backward

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_backward = Button(root, text="<<", command=lambda: backward(image_number-1))
	
	if image_number == 5:
		button_forward = Button(root, text=">>", state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_backward.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)

def backward(image_number):
	global my_label
	global button_forward
	global button_backward

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_backward = Button(root, text="<<", command=lambda: backward(image_number-1))

	if image_number ==1:
		button_backward = Button(root, text="<<", state=DISABLED)
	
	my_label.grid(row=0, column=0, columnspan=3)
	button_backward.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)

button_backward = Button(root, text="<<", command=lambda: backward)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_backward.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
