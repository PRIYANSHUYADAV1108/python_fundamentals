class laptop:
    storage_type = "ssd"
    def __init__(self,ram,storage):
        self.ram = ram
        self.storage = storage
    @classmethod 	
    def get_info_type(cls):
        print(f"storage type = {cls.storage_type}")

l1 = laptop("12gb","512gb")

l1.get_info_type()
