print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
def read_last_n_lines(file_path, n):
    """Đọc và in ra n dòng cuối cùng của tệp."""
    try:
        # Đọc tất cả các dòng vào một danh sách
        with open(file_path, 'r', encoding='utf-8') as f:
            # Phương thức .readlines() đọc tất cả các dòng và trả về dưới dạng list
            all_lines = f.readlines()
            
        # Lấy n dòng cuối cùng (Sử dụng Python list slicing)
        # Nếu n lớn hơn số dòng thực tế, nó sẽ lấy toàn bộ list (từ đầu đến cuối)
        last_n_lines = all_lines[-n:]
        
        # In các dòng cuối cùng ra màn hình
        for line in last_n_lines:
            # end='' giúp không thêm ký tự xuống dòng vì readline() đã đọc cả ký tự xuống dòng gốc
            print(line, end='')

    except FileNotFoundError:
        # Xử lý lỗi nếu không tìm thấy file
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")

    except Exception as e:
        # Xử lý các lỗi khác
        print(f"Đã xảy ra lỗi: {e}")

# Định nghĩa đường dẫn file và số dòng cần đọc
file_duong_dan = 'D:/b.txt'
so_dong = 3 

# Gọi hàm để đọc n dòng cuối cùng
read_last_n_lines(file_duong_dan, so_dong)
