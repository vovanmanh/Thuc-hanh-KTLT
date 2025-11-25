print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Số dư hiện tại: {self.balance} VND")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Đã nạp {amount} VND")
        else:
            print("Số tiền không hợp lệ!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Đã rút {amount} VND")
        else:
            print("Số dư không đủ hoặc số tiền không hợp lệ!")

atm = ATM(1000) 
atm.check_balance()
atm.deposit(500)
atm.withdraw(300)
atm.check_balance()
