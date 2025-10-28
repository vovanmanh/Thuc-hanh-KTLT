print("Sinh vien:Vo Van Manh")
print("Ma so SV:245752021610011")
print("#########################")
#########################
def get_sum(*num):
 tmp = 0
 # duyet cac tham so
 for i in num:
   tmp += i
 return tmp
result = get_sum(1, 2, 3, 4, 5)
print(result)


