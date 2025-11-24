print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
def tim_vi_tri_max_min(ds):
    max_val = max(ds)
    min_val = min(ds)
    vi_tri_max = ds.index(max_val)
    vi_tri_min = ds.index(min_val)
    return vi_tri_max,vi_tri_min

n = int(input("Nhap so phan tu:"))
ds = []
for i in range(n):
    x = int(input(f"nhap phan tu thu {i+1}:"))
    ds.append(x)

vt_max,vt_min = tim_vi_tri_max_min(ds)

print("Vi tri phan tu lon nhat:",vt_max)
print("Vi tri phan tu nho nhat:",vt_min)
