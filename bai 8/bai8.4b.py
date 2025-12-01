print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
from tkinter import *

def clicked():
    lbl.configure(text="Button was clicked !!")

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0) 

window.mainloop()
