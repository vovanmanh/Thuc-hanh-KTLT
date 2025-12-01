print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
from tkinter import *
from tkinter import messagebox

def OpenFile():
    messagebox.showinfo("Chức năng File", "Thực hiện chức năng Mở/Tạo File mới!")

def Exit():
    if messagebox.askyesno("Thoát", "Bạn có chắc chắn muốn thoát ứng dụng không?"):
        root.quit()

def InsText():
    messagebox.showinfo("Chèn", "Thực hiện chức năng Chèn Văn bản.")

def InsPic():
    messagebox.showinfo("Chèn", "Thực hiện chức năng Chèn Hình ảnh.")

def About():
    messagebox.showinfo("Về Ứng Dụng", "Đây là ứng dụng Tkinter Menu Demo.")

root = Tk()
root.title("tk")
root.geometry('300x150')

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=OpenFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)

insertMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertMenu)
insertMenu.add_command(label="Text", command=InsText)
insertMenu.add_command(label="Picture", command=InsPic)

helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

root.mainloop()
