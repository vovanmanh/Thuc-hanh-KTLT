print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
def append_and_display_file(file_path, text_to_append):
    """Nối văn bản vào cuối tệp, sau đó đọc và in ra toàn bộ nội dung."""
    
    # --- 1. Nối (thêm) văn bản vào cuối file ---
    print(f"Lần chạy 1: Khởi tạo tệp.") # Dòng này hiển thị trong lần chạy đầu tiên

    try:
        # Mở file với chế độ 'a' (append) để thêm nội dung vào cuối
        with open(file_path, 'a', encoding='utf-8') as myfile:
            # Ghi nội dung cần thêm vào file, kèm thêm ký tự xuống dòng '\n'
            myfile.write(text_to_append + '\n')
            
    except Exception as e:
        # Xử lý lỗi trong quá trình ghi file
        print(f"Lỗi khi ghi file: {e}")
        return # Dừng hàm nếu ghi file thất bại

    # --- 2. Đọc và hiển thị toàn bộ nội dung file ---
    try:
        # Mở file với chế độ 'r' (read) để đọc toàn bộ
        with open(file_path, 'r', encoding='utf-8') as myfile:
            content = myfile.read()
            
            # In tiêu đề và nội dung
            print("\n--- Nội dung tệp sau khi nối ---")
            print(content)
            print("---------------------------------")
            
    except FileNotFoundError:
        # Trường hợp này hiếm xảy ra sau khi vừa ghi thành công
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")
        
    except Exception as e:
        # Xử lý các lỗi khác
        print(f"Đã xảy ra lỗi: {e}")

# --- Thiết lập tham số ---
file_duong_dan = 'abc.txt'
noi_dung_them = "Đây là dòng được thêm vào sau."

# --- Thực thi lần 1 (Tạo và thêm nội dung) ---
print(f"\nLần chạy 1: Khởi tạo tệp.")
append_and_display_file(file_duong_dan, "Python là ngôn ngữ lập trình.")

# --- Thực thi lần 2 (Thêm nội dung mới) ---
print(f"\nLần chạy 2: Nối thêm văn bản.")
append_and_display_file(file_duong_dan, noi_dung_them)
