print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
class MyString:
    def get_String(self):
        self.s = input("Nhập chuỗi: ")

    def print_String(self):
        print(self.s.upper())

obj = MyString()
obj.get_String()
obj.print_String()
