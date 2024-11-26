
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
item2 = Item("laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
