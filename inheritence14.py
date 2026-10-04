class employee:
    start_time = "10AM"
    end_time = "5PM"
class teacher(employee): #inheritence
    def __init__(self,subject):
        self.subject = subject

t1 = teacher("DSA")

print(t1.subject,t1.start_time, t1.end_time)
