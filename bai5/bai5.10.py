print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
def bubbleSort(nlist):
    """
    Thuật toán sắp xếp nổi bọt (bubble sort).
    Sắp xếp danh sách theo thứ tự tăng dần.
    """
    n = len(nlist)
    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if nlist[j] > nlist[j + 1]:
                # Hoán đổi
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
    return nlist
n = int(input("Nhập số phần tử: "))


nlist = []
for i in range(n):
    val = int(input(f"Nhập phần tử thứ {i}: "))
    nlist.append(val)

print("\nDanh sách trước khi sắp xếp:", nlist)

sorted_list = bubbleSort(nlist)

print("Danh sách sau khi sắp xếp:", sorted_list)
