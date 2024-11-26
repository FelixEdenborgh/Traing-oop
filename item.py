
class Item:
    pay_rate = 0.8 # The pay rate after 20% discount

    def __init__(self, name: str, price: int, quantity: int = 0):
        print(f"Item created for {name}")

        # Run validation to the recived arguments
        assert price >= 0, f"Price {price} is not greater then zero!"
        assert quantity >= 0, f"Quantity {quantity} cannot be 0!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item("Phone", 100, 5)
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))
print(type(item1))

print(item1)
print(item1.name)
print(item1.price)
print(item1.quantity)
print(item1.calculate_total_price())

item2 = Item("Phone x1", 250, 5)
item2.name = "Phone x1"
item2.price = 250
item2.quantity = 5

print(item2)
print(item2.name)
print(item2.price)
print(item2.quantity)
print(item2.calculate_total_price())

item3 = Item("Iphone xs", 1000, 3)
print(item3)
print(item3.name)
print(item3.price)
print(item3.quantity)
print(item3.calculate_total_price())

print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)

print(Item.__dict__) # All the attributes for class level
print(item1.__dict__) # All the attributes for instance level
print(item2.__dict__) # All the attributes for instance level

item1.apply_discount()
print(item1.price)

item2.pay_rate = 0.1
item2.apply_discount()
print(item2.price)