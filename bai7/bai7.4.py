print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
def read_first_n_lines(file_path, n):
    """Đọc và in ra n dòng đầu tiên của tệp."""
    try:
        # Mở file để đọc ('r'), sử dụng encoding='utf-8'
        with open(file_path, 'r', encoding='utf-8') as f:
            # Lặp lại n lần (tương ứng với n dòng đầu tiên)
            for i in range(n):
                # Đọc từng dòng một
                line = f.readline()
                
                # Kiểm tra nếu đã hết file (line rỗng)
                if not line:
                    # Dừng nếu đã hết file trước khi đạt đến n dòng
                    break
                
                # In dòng đó ra. end='' giúp không thêm ký tự xuống dòng
                # vì readline() đã đọc cả ký tự xuống dòng gốc của file
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

# Gọi hàm để đọc n dòng đầu tiên
read_first_n_lines(file_duong_dan, so_dong)
