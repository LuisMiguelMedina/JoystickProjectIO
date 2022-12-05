from tkinter import *

root = Tk()

#Create a lavel widget
def myClick():
    myLabel = Label(root, text = "hello world!").grid(row=2, column=2)
    myLabel.pack()
# Button
mybutton = Button(root, text = "Click me!", pady=150, command=myClick)
mybutton.pack()

# bg="" -> background colors
# fg="" -> letter colors

root.mainloop()