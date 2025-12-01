print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
import turtle


window = turtle.Screen()
window.bgcolor("white")
window.title("Hoa Văn Hình Tròn")

painter = turtle.Turtle()
painter.pensize(2)
painter.speed(0) 

colors = ["red", "green", "blue"]

angle_per_circle = 360 / 18 

for i in range(18): 
    color_index = i % 3 
    current_color = colors[color_index]
    
    painter.pencolor(current_color)

    painter.circle(80)

    painter.left(angle_per_circle)

window.mainloop()
