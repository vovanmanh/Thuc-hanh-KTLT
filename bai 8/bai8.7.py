print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
import tkinter
import random
from tkinter import messagebox
colours = ['Red','Blue','Green','Pink','Black',
'Yellow','Orange','White','Purple','Brown']
score = 0
timeleft = 120
game_started = False 
def startGame(event):
    global timeleft
    global game_started
    if not game_started:
        game_started = True
        timeleft = 120
        global score
        score = 0
        scoreLabel.config(text = "Score: " + str(score))
        countdown()
        nextColour()
def nextColour():
    global score
    global timeleft
    if timeleft > 0 and game_started:
        e.focus_set()
        correct_colour = colours[1].lower()
        if e.get() != "":
            if e.get().lower() == correct_colour:
                score += 2
            else:
                score -= 1
            e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg = str(colours[1]), text = str(colours[0]))
        scoreLabel.config(text = "Score: " + str(score))
        e.focus_set()
def countdown():
    global timeleft
    global game_started
    if timeleft > 0 and game_started:
        timeleft -= 1
        timeLabel.config(text = "Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)
    elif timeleft <= 0 and game_started:
        game_started = False
        timeleft = 0
        timeLabel.config(text = "Time left: 0", fg="red")
        messagebox.showinfo("Game Over!", "Trò chơi kết thúc! Điểm số của bạn là: {s}".format(s=score))
root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("375x250") 
root.resizable(False, False)
instructions = tkinter.Label(root, 
                            text = "Gõ tên MÀU của chữ, KHÔNG phải văn bản được hiển thị!\nNhấn ENTER để bắt đầu.",
                            font = ('Helvetica', 12))
instructions.pack(pady=5)
scoreLabel = tkinter.Label(root, text = "Nhấn ENTER để bắt đầu",
font = ('Helvetica', 12))
scoreLabel.pack(pady=5)
timeLabel = tkinter.Label(root, text = "Time left: " + str(timeleft), 
                        font = ('Helvetica', 12))
timeLabel.pack(pady=5)
label = tkinter.Label(root, font = ('Helvetica', 60, 'bold'))
label.pack(pady=10)
e = tkinter.Entry(root, justify='center', width=30, font=('Helvetica', 12))
e.bind('<Return>', nextColour)
e.pack(pady=10)

root.bind('<Return>', startGame)

e.focus_set()

root.mainloop()
