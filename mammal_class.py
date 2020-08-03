class Mammal:
    def __init__(self, name, type_of_mammal, breed, legs):
        self.name = name
        self.type_of_mammal = type_of_mammal
        self.breed = breed
        self.legs = legs

    def eat(self):
        return "%s is eating" % (self.name)


class Cat(Mammal):
    def __init__(self, name, type_of_mammal, breed, legs, fur):
        super().__init__(name, type_of_mammal, breed, legs)
        self.fur = fur

    def __str__(self):
        return "%s is a %s %s with %d legs and %s fur" % (self.name, self.type_of_mammal, self.breed, self.legs, self.fur)

    def purr(self):
        return "%s is purring" % (self.name)

    def eat(self):
        return "The cat eats differently for reasons!!!"


guster = Cat("Gus", "cat", "mixed", 4, "short hair")
harry = Mammal("Harry", "dog", "lab", 4)

print(guster)

print(guster.purr())
print(guster.eat())
print(harry.eat())
