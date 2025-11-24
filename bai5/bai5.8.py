print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
def sequential_search(dlist,item):
    pos = 0
    found = False

    while pos < len(dlist) and found == False:
        if dlist[pos] == item:
            found = True
        else:
            pos += 1

    return found, pos if found else -1

dlist = list(map(int,input("Nhap danh sach (cac so cach nhau boi dau cach):").split()))
item = int(input("NNhap phan tu can tim:"))

found,pos = sequential_search(dlist,item)
if found:
     print(f"Tim thay {item} tai vi tri {pos}")
else:
     print(f"Khong tim thay {item} trong danh sach")
