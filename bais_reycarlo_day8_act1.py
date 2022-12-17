class Car():
    color = "brown"
    model = "boxtype 1990"
    manufacturer = "Honda"
    def sound(self):
        print("Broom broom!")

car1 = Car()

print(f"""Manufacturer: {car1.manufacturer}
Model: {car1.model}
Color: {car1.color}""")

car2 = Car()
car2.color = "silver"
car2.model = "SUV 2006"
car2.manufacturer = "Kia"
print(f"""\nManufacturer: {car2.manufacturer}
Model: {car2.model}
Color: {car2.color}""")

print(f"\nSound: {car1.sound()}")