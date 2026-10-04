class BankAccount:
    def __init__(self,name,balance):
        self.name = name 
        self.__balance = balance #private attribute
acc1 = BankAccount("priyanshu", 10000000000)
print(acc1.name) #private atrribute cannot accessed by acc1.__balance
