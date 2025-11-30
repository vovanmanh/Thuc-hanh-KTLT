print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
def reverse_file_contents(file_path):
    """Đọc file và in nội dung của từng dòng theo thứ tự đảo ngược."""
    try:
        # Mở file để đọc ('r')
        with open(file_path, 'r') as input_file:
            for line in input_file:
                # Bỏ ký tự xuống dòng ở cuối ('\n') rồi dùng slicing [::-1] để đảo ngược chuỗi
                reversed_line = line.rstrip('\n')[::-1]
                print(reversed_line)

    except FileNotFoundError:
        # Xử lý lỗi nếu không tìm thấy file
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")

    except Exception as e:
        # Xử lý các lỗi khác
        print(f"Đã xảy ra lỗi: {e}")

# Định nghĩa đường dẫn file
file_duong_dan = 'D:/a.txt' 

# Gọi hàm để thực hiện việc đảo ngược nội dung file
reverse_file_contents(file_duong_dan)
