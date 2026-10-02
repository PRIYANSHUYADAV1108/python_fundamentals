class laptop:
    storage_type = "ssd"
    def __init__(self,ram,storage):
        self.ram = ram
        self.storage = storage
    @classmethod 	
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")

    def get_info(self):
        print(f"laptop has {self.ram}Ram & {self.storage}, {self.storage_type}")

    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (discount * (price/100))
        print(f"discount price = {final_price}")	


l1 = laptop("12gb","512gb")

l1.calc_discount(40000,10)
