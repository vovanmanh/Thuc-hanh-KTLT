print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
import turtle
window = turtle.Screen()
window.bgcolor("lightblue") 

painter = turtle.Turtle()
painter.color('red', 'yellow') 
painter.pensize(2)

def drawsq(t, s):
    """
    Vẽ một hình vuông với cạnh dài s sử dụng rùa t.
    """
    t.begin_fill()
    for _ in range(4):
        t.forward(s)
        t.left(90)
    t.end_fill()

painter.speed(0) 

for i in range(18): 
    painter.left(20) 
    drawsq(painter, 100) 

window.mainloop()
