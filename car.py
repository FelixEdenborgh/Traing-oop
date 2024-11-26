class Car:
    num_cars = 0
    numberOfWeels = 4 # class variable
    def __init__(self, model, brand, wheelSize, year, color):
        self.model = model
        self.brand = brand
        self.weelSize = wheelSize
        self.year = year
        self.color = color
        Car.num_cars += 1

    def drive(self):
        print(f"The {self.color} car {self.model} are driving")

    def stop(self):
        print(f"The {self.color} car {self.model} have stoped")



car1 = Car("bmw320", "BMW", 18, 2008, "Black")
car2 = Car("Audi A4 Quatro", "Audi", 22, 2008, "Silver")

print(Car.num_cars)
print(Car.numberOfWeels)

print(car1.drive())
print(car2.stop())
