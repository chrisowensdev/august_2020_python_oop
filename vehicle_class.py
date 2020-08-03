class Vehicle:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return "Make: %s, Model: %s, Year: %d, Color: %s" % (self.make, self.model, self.year, self.color)

    def wheels(self, wheels):
        return "Wheels: %s" % wheels


# Make Model, Year
# Instantiate the class
honda = Vehicle("Honda", "Civic", 1998, "Silver")

print(honda)

print(honda.wheels(4))
