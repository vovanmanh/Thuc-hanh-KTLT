print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
s = input().strip()

items = s.split(',')

result = []

for b in items:
    num = int(b, 2)
    if num % 5 == 0:
        result.append(b)

print(','.join(result))
