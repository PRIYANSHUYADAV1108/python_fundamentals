class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance
    def get_balance(self): # getter function
       return self.__balance

acc1 =BankAccount("Priya Yadav", 1000000)

print(acc1.name, acc1.get_balance)

