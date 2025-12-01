print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################

import tkinter as tk

root = tk.Tk()
root.title("Radio Button Demo")

v = tk.IntVar()
v.set(1)

languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

def ShowChoice():
    """In ra giá trị (value) của Radio Button hiện đang được chọn."""
    print("Giá trị đã chọn: {v.get()}".format(v=v))

tk.Label(
    root,
    text="Chọn ngôn ngữ lập trình yêu thích của bạn:",
    justify=tk.LEFT, 
    padx=20 
).pack()

for text, val in languages:
    tk.Radiobutton(
        root,
        text=text, 
        padx=20,
        variable=v, 
        command=ShowChoice, 
        value=val 
    ).pack(anchor=tk.W) 

root.mainloop()
