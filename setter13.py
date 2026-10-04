class BankAccount:
    def __init__(self,name,balance):
      self.name = name
      self._balance = balance
    def get_balance(self):
       return self._balance
    def set_balance(self,new_balance):
      self._balance = new_balance

acc1 = BankAccount("priya", 1000000)
acc1.set_balance(200000)

print(acc1.name, acc1.get_balance())
