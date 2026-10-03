class product_store:
    count = 0
    def __init__(self,name):
        self.name = name
	
        product_store.count =+1

    def get_info(self):
	 print(f"product name {self.name} & price is = ")

    @classmethod
    def get_count(cls):
	 print(f"the product count is {cls.count}")

    @staticmethod
    def get_discount(price,discount):
	 print(f"discount_price = {price - (price * (discount/100))}")

p1 = product_store("phone")
p2 = product_store("laptop")
p3 = product_store("pen")


p1.get_info()


p2.get_info()


