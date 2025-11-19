print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
import math

def Tinh(R):
    if R <= 0:
        print("Bán kính không hợp lệ, phải lớn hơn 0!")
        return
    
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R * R

    print("Chu vi hình tròn =", chu_vi)
    print("Diện tích hình tròn =", dien_tich)


r = float(input("Nhập bán kính R: "))
Tinh(r)
