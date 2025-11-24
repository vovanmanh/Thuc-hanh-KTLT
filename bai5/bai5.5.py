print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
danh_sach = []
while True:
    try:
        so_luong = int(input("Nhap so luongphan tu (N):"))
        if so_luong > 0:
            break
        else:
            print("so luong phai la mot so nguyen duong.")
    except ValueError:
          print("Vui long nhap mot so nguyen hop le.")
for i in range(so_luong):
                while True:
                    try:
                        gia_tri = int(input(f"nhap gia tri thu {i+1}:"))
                        danh_sach.append(gia_tri)
                        break
                    except ValueError:
                        print("Vui long nhap mot so nguyen hop le.")
if danh_sach:
    max_value = max(danh_sach)
    min_value = min(danh_sach)

    print("\n--- KET QUA ---")
    print(f"Danh sach da nhap:{danh_sach}")
    print(f"Phan tu lon nhat (Max) : {max_value}")
    print(f"Phan tu nho nhat (Min) : {min_value}")
else:
    print("Danh sach rong, khong the tim Min/Max.")
    
          
