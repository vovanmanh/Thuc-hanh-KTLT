print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
import tkinter as tk
from tkinter import ttk
def create_personal_info_form():
    form = tk.Toplevel()
    form.title("Thông tin cá nhân")
    form.geometry("420x250")
    tk.Label(
        form, 
        text="THÔNG TIN CÁ NHÂN",
        font=("Arial", 16, "bold"),
        fg="blue"
    ).grid(row=0, column=0, columnspan=2, pady=10)
    labels = ["Họ và tên:", "Ngày sinh:", "MSSV:", "Ngành học:"]
    values = ["VÕ VĂN MẠNH", "02/04/2006", "245752021610011", "KTCK VÀ TDH"]
    for row, (label, value) in enumerate(zip(labels, values), start=1):
        tk.Label(form, text=label, font=("Arial", 12)).grid(
            row=row, column=0, sticky="w", padx=10
        )
        tk.Label(form, text=value, font=("Arial", 12, "bold")).grid(
            row=row, column=1, sticky="w"
        )
root = tk.Tk()
root.title("Bài Tập Tkinter")
root.geometry("400x150")

tk.Label(root, text="Bấm để mở Form:", font=("Arial", 12)).pack(pady=10)

tk.Button(
    root,
    text="Mở Form Thông tin Cá nhân",
    font=("Arial", 12),
    command=create_personal_info_form
).pack(pady=10)

root.mainloop()
