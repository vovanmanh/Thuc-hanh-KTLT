print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
chuoi_nhap = input("Nhap cac tu tieng Anh (cach nhau dau cach):")
ds_tu = chuoi_nhap.split()

ds_tu.sort()

print(",".join(ds_tu))
