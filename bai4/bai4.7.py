print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
S = input("Nhap chuoi co lan so:")
S_moi = ""

for ch in S:
    if not ch.isdigit():
        S_moi=S_moi+ch

print(f"chuoi sau khi loai bo so: {S_moi}")        
