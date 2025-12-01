print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
from tkinter import *

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x100')

lbl_key = Label(window, text="Bấm phím bất kỳ trên cửa sổ này!", font=("Arial", 12))
lbl_key.grid(column=0, row=0, padx=10, pady=10)

def key_pressed(event):
    """Xử lý sự kiện khi một phím trên bàn phím được bấm."""
    
    key_info ="Bạn đã bấm phím: '{}'".format(event.char)
    lbl_key.configure(text=key_info)

window.bind("<Key>", key_pressed)

window.mainloop()
