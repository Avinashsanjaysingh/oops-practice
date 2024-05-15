
class Item:
    def __init__(self,name: str,price:float,quantity=0):    #quantity=0 is a default parameter & we do not neccessarily need to pass this argument.
        # print(f"An instance created: {name}")
        self.name = name 
        self.price = price
        self.quantity = quantity

    # def calculate_total_price(self, x, y):
    #     return x*y
    def calculate_total_price(self):
        return self.price * self.quantity
    

item1 = Item(1,100,5) # if we pass numbers as string "100" then it will perform string operation like- "100",5 100100100100100
# item1.name = "Phone"    # line 5
# item1.price = 100   # line 6
# item1.quantity = 5  # line 7
# print(item1.calculate_total_price(item1.price, item1.quantity))

# random_str = "aaa"
# print(random_str.upper())

item2 = Item("Laptop",1000,3)
# item2.name = "Phone"    # line 5
# item2.price = 100   # line 6
# item2.quantity = 5  # line 7
# print(item1.calculate_total_price(item2.price, item2.quantity))
item2.has_numpad = False


print(item1.name)
# print(item2.name)
# print(item1.price)
# print(item2.price)
# print(item1.quantity)
# print(item2.quantity)
print(item1.calculate_total_price())
print(item2.calculate_total_price())


