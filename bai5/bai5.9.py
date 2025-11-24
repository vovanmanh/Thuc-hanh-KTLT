print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
def binary_search(lst,value):
    lowerBound = 0
    upperBound = len(lst) - 1

    while lowerBound <= upperBound:
        midPoint = (lowerBound + upperBound) // 2

        if lst[midPoint] == value:
            return True
        elif lst[midPoint] < value:
            lowerBound = midPoint + 1
        else:
            upperBound = midPoint - 1

    return False
lst = list(map(int,input("Nhap list (cac so cah nhau boi khoang trang):").split()))
lst.sort()
print("list sau khi sap xep:",lst)

value = int(input("Nhap gia tri can tim:"))

result = binary_search(lst,value)
print("Ket qua:",result)
           


