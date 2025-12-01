print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
def tinh_so_tien_thuc():
    # Khởi tạo số dư ban đầu
    so_du = 0 
    
    print("\nHướng dẫn:")
    print("1. Nhập giao dịch: **D <số_tiền>** (Gửi tiền) hoặc **W <số_tiền>** (Rút tiền).")
    print("2. Nhập **'kết thúc'** để dừng nhập liệu và tính số dư cuối cùng.")
    print("---")

    while True:
        giao_dich = input("Giao dịch (D/W <số_tiền>): ").strip()
        
        if giao_dich.lower() == 'kết thúc':
            break

        phan_tu = giao_dich.split()
        
        if len(phan_tu) != 2:
            print("Lỗi: Định dạng giao dịch không hợp lệ. Vui lòng nhập đúng cú pháp.")
            continue
            
        loai_giao_dich = phan_tu[0].upper() 
        
        try:
            so_tien = int(phan_tu[1])
        except ValueError:
            print("Lỗi: Số tiền không hợp lệ. Vui lòng nhập một số nguyên dương.")
            continue
            
     
        if loai_giao_dich == 'D': 
            so_du += so_tien
            print(f"-> Đã gửi: {so_tien}. Số dư tạm thời: {so_du}")
            
        elif loai_giao_dich == 'W': 
            so_du -= so_tien
            print(f"-> Đã rút: {so_tien}. Số dư tạm thời: {so_du}")
            
        else:
            print("Lỗi: Loại giao dịch không hợp lệ. Chỉ chấp nhận 'D' hoặc 'W'.")

tinh_so_tien_thuc()
