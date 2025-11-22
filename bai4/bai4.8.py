print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
s = input("Nhập dãy từ: ")

words = s.split()

max_len = max(len(w) for w in words)

print("Các từ dài nhất:")
for w in words:
    if len(w) == max_len:
        print(w)
