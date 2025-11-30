print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
def read_entire_file(file_path):
    """Đọc và in ra toàn bộ nội dung của tệp."""
    try:
        # Mở file để đọc ('r'), sử dụng encoding='utf-8' để xử lý tiếng Việt
        with open(file_path, 'r', encoding='utf-8') as f:
            # Đọc toàn bộ nội dung file vào biến 'content'
            content = f.read()
            # In nội dung ra màn hình
            print(content)
            
    except FileNotFoundError:
        # Xử lý lỗi nếu không tìm thấy file
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")

    except Exception as e:
        # Xử lý các lỗi khác
        print(f"Đã xảy ra lỗi: {e}")

# Định nghĩa đường dẫn file
file_duong_dan = 'D:/a.txt' 

# Gọi hàm để đọc và in nội dung file
read_entire_file(file_duong_dan)
