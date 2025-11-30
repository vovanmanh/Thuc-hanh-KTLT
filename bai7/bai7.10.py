print("Sinh vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
import re
import os
def find_longest_words(file_path):
    """
    Tìm và in ra những từ có độ dài lớn nhất trong tệp.
    """
    longest_length = 0
    longest_words = []

    try:
        if not os.path.exists(file_path):
            print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")
            return

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        words = re.findall(r'\b\w+\b', content.lower())

        if not words:
            print("Tệp không chứa từ nào.")
            return

        for word in words:
            word_length = len(word)

            if word_length > longest_length:
                longest_length = word_length
                longest_words = [word]
            elif word_length == longest_length:
                if word not in longest_words: 
                    longest_words.append(word)

       
        print("\n" + "#" * 30)
        print(f"Độ dài của từ dài nhất là: {longest_length} ký tự.")
        print(f"Các từ dài nhất là:")
        for word in sorted(longest_words): 
            print(f"- {word}")
        print("#" * 30)

    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
find_longest_words('D:/c.txt') 
