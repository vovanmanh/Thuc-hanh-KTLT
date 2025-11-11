print("Sinh vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
import re
passwords = input("nhap cac mat khau ,cach nhau bang dau phay:").split(',')

valid_passwords=[]

for p in passwords:
    p=p.strip()

    if len(p)<6 or len(P)>12:
        continue

    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    valid_passwords.append(p)

 print("mat khau hop le:",",".join(valid_passwords))
