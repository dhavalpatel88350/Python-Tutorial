class Bank:
    balance=5000
    def login(self,pin):
        if pin==1111:
            return True
        else:
            return False
    def credit(self,amt):
        self.balance+=amt
    def debit(self,amt):
        self.balance-=amt
    def display(self):
        print("Current balance is "+str(self.balance))
obj = Bank()
flag=False
for i in range(1,4):
       if obj.login(int(input("enter pin code"))):
           flag=True
           break
if flag:
  while True:
     o=input("""
             Press c for credit
             Press d for debit
             Press b for balance
             Press e for exit""") 
     if o=='c' or o=='C':
      obj.credit(int(input("enter amount for credit")))
      print("After credit total amount is ")
      obj.display()
     elif o=='d' or o=='D':
      amt=int(input("enter amount for debit"))
      if amt<obj.balance:
       obj.debit(amt)
       print("After debit total amount is ")
      else:
       print("insufficient balance")
      obj.display()
     elif o=='b' or o=='B':
      print("Total balance is ")
      obj.display()
     elif o=='e' or o=='E':
       exit(0)
else:
        print("Your pin code attempt has been completed")