class employee:
    start_time = "10Am"
    end_time = "5PM"

class adminstaff(employee):
    def __init__(self,role):
        self.role = role

class accountant(adminstaff):
    def __init__(self,salary,role):
        super().__init__(role)
        self.salary = salary

acc1 = accountant(250000,"CA")
print(acc1.role, acc1.salary,acc1.start_time, acc1.end_time)
    
