print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
def count_file_stats(file_path):
    """Đọc file và tính số ký tự, số từ, và số dòng."""
    char_count = 0
    word_count = 0
    line_count = 0

    try:
        # Mở file để đọc ('r') với quản lý ngữ cảnh 'with open...'
        with open(file_path, 'r') as f:
            for line in f:
                # 1. Đếm số dòng
                line_count += 1
                
                # 2. Đếm số ký tự (bao gồm khoảng trắng và ký tự xuống dòng)
                char_count += len(line)
                
                # 3. Đếm số từ
                # Loại bỏ khoảng trắng thừa ở đầu/cuối và ký tự xuống dòng bằng .strip()
                # Sau đó dùng .split() để tách thành danh sách các từ
                words = line.strip().split()
                # Cộng thêm số lượng từ trong danh sách đó
                word_count += len(words)

        # In kết quả thống kê sau khi duyệt hết file
        print(f"Số ký tự (bao gồm khoảng trắng và ký tự xuống dòng) là: {char_count}")
        print(f"Số từ là: {word_count}")
        print(f"Số dòng là: {line_count}")

    except FileNotFoundError:
        # Xử lý khi không tìm thấy file
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")

    except Exception as e:
        # Xử lý các lỗi khác ngoài lỗi không tìm thấy file
        print(f"Đã xảy ra lỗi: {e}")

# Định nghĩa đường dẫn file
file_duong_dan = 'D:/a.txt' 

# Gọi hàm để thực hiện thống kê file
count_file_stats(file_duong_dan)
