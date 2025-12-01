print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
def loc_so_le():
    chuoi_so = input("Nhập các số, cách nhau bởi dấu cách: ")
    ds_chuoi_so = chuoi_so.split()
    
    ds_so_le = []
    
    for chuoi_so_hien_tai in ds_chuoi_so:
        try:
            so = int(chuoi_so_hien_tai)
            # Kiểm tra nếu là số lẻ (số dư khác 0 khi chia cho 2)
            if so % 2 != 0:
                ds_so_le.append(so)
        except ValueError:
            # Bỏ qua nếu có kí tự không phải số
            continue
            
    print("Danh sách các số lẻ đã lọc:", ds_so_le)

loc_so_le()
