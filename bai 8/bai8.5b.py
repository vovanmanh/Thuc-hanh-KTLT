print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
import tkinter as tk
root = tk.Tk()
root.title("tk")

v = tk.IntVar()
v.set(1)

languages = [
    ("Python 1", 1), 
    ("Perl 2", 2),
    ("Java 3", 3),
    ("C++ 4", 4),
    ("C 5", 5)
]

def ShowChoice():
    print("Giá trị đã chọn: {v.get()}".format(v=v))

tk.Label(
    root,
    text="Choose your favourite \nprogramming language:",
    justify=tk.LEFT,
    padx=20,
    bg="lightgray" 
).pack(fill=tk.X)

for text, val in languages:
    tk.Radiobutton(
        root,
        text=text,
        padx=20,
        variable=v,
        command=ShowChoice,
        value=val,
        indicatoron=0,
        width=20, 
        anchor=tk.W, 
        bd=1,
        relief=tk.RIDGE 
    ).pack(fill=tk.X)

root.mainloop()
