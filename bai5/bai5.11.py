print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
import numpy as np

data = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
]

dt = np.dtype([
    ('name', 'U20'),
    ('class', 'i4'),
    ('height', 'f4')
])

students = np.array(data, dtype=dt)

sorted_students = np.sort(students, order=['class', 'height'])

print(sorted_students)
