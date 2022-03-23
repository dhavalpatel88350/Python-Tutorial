class ATM():
    d=2000
    def balance(self,amt):
        self.x=ATM.d
        return self.x
    def deposit(self,amt):
        w=500
        self.x+w
        return self.x
    def withdraw(self,amt):
        self.x-=300
        return self.x
obj=ATM()
p=int(input("enter for check:/enter 2 for diposit ://enter 3 for withdraw/"))
if p==1:
    print(obj.balance())
elif p==2:
    print(obj.deposit())
elif p==3:
    print(obj.withdraw())
else:
    print("i number")

