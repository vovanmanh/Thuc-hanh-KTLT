print("Sinh vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
from tkinter import *

def clicked():
    lbl.configure(text="Màu của Button đã được thay đổi!")

window = Tk()
window.title("Thay Đổi Màu Button")
window.geometry('350x150')

lbl = Label(window, text="Nhấn nút để kiểm tra màu sắc")
lbl.grid(column=0, row=0, padx=10, pady=10)

btn = Button(
    window,
    text="Click Me",
    command=clicked,
    bg="green", 
    fg="white", 
    font=("Arial", 10, "bold")
)

btn.grid(column=0, row=1, padx=10, pady=5)

window.mainloop()
