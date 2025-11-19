
print("Sinh vien:Vo Van Manh")
print("Ma so SV:245752021610011")
print("#########################")
#########################
import math

pos = [0, 0]   

while True:
    s = input()
    if not s:
        break
    try:
       movement = s.split()
       direction = movement[0]
       steps = int(movement[1])
    except (IndexError,ValueError):
          continue
    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps
    else:
        pass

distance = math.sqrt(pos[0]**2 + pos[1]**2)
print(round(distance))



