print("Sinh vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
def benefit(t, n, k):
    if t < 0 or n <= 0 or k < 0:
        print("Dữ liệu không hợp lệ!")
        return

    amount = n * (1 + t/100) ** k
    return amount


# Nhập dữ liệu
t = float(input("Nhập lãi suất t (%/tháng): "))
n = float(input("Nhập số vốn ban đầu n: "))
k = int(input("Nhập số tháng gửi k: "))

# Gọi hàm
result = benefit(t, n, k)

# Định dạng tiền tệ (có dấu phẩy)
formatted = "{:,.0f} VND".format(result)

print("Số tiền nhận được sau", k, "tháng là:", formatted)
