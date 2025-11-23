print("Sinh vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
def pascal_rows(n):
    row = []
    for i in range(n):
        if i == 0:
            row = [1]
        else:
            # tạo hàng mới từ hàng trước
            new_row = [1]
            for j in range(len(row)-1):
                new_row.append(row[j] + row[j+1])
            new_row.append(1)
            row = new_row
        print(' '.join(str(x) for x in row))

if __name__ == "__main__":
    n = int(input().strip())
    if n <= 0:
        pass
    else:
        pascal_rows(n)
