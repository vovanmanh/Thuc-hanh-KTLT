print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
import tkinter as tk
from tkinter import messagebox

def show_choice():
    choice = selected.get()     
    messagebox.showinfo("Kết quả", f"Bạn chọn nút radio: {choice}")
root = tk.Tk()
root.title("Radio Button Demo")
root.geometry("300x200")

tk.Label(root, text="Hãy chọn một tùy chọn:", font=("Arial", 12)).pack(pady=10)

selected = tk.IntVar()
selected.set(1)  

tk.Radiobutton(root, text="Option 1", variable=selected, value=1, font=("Arial", 11)).pack()
tk.Radiobutton(root, text="Option 2", variable=selected, value=2, font=("Arial", 11)).pack()
tk.Radiobutton(root, text="Option 3", variable=selected, value=3, font=("Arial", 11)).pack()

tk.Button(root, text="Click Me", font=("Arial", 12), command=show_choice).pack(pady=15)

root.mainloop()
