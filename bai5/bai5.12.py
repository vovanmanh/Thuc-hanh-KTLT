print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
import numpy as np

student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40., 42., 45., 41., 38., 40., 42.0])

indices = np.lexsort((student_id, student_height))

print("Chỉ số:")
print(indices)

print("Dữ liệu sắp xếp:")
for i in indices:
    print(student_id[i], student_height[i])
