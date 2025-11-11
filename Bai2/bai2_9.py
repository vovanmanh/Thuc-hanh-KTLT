print("Sinh vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
str=input("Enter a String:")
dict = {}
for n in str:
    keys = dict.keys()
    if n in keys :
        dict [n] += 1
    else :
         dict[n] = 1
print (dict)         
