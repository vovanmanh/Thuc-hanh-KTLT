print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
class Hinhchunhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def dien_tich(self):
        return self.dai * self.rong

hcn = Hinhchunhat(5, 3)
print("Diện tích:", hcn.dien_tich())
