class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness

    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30

    def be_alive(self, hunger, mopiness):
        self.fullness -= hunger
        self.happiness -= mopiness

    def __str__(self):
        return """
        %s:
        Fullness: %d
        Happiness: %d
        Hunger: %d
        Mopiness: %d
        """ % (self.name, self.fullness, self.happiness, self.hunger, self.mopiness)


class CuddlyPet(Pet):
    def __init__(self, name, fullness=50, hunger=5, cuddle_level="Cuddly"):
        super().__init__(name, fullness, 100, hunger, 1)
        self.cuddle_level = cuddle_level

    def __str__(self):
        return """
        %s:
        Fullness: %d
        Happiness: %d
        Hunger: %d
        Cuddle Level: %s
        """ % (self.name, self.fullness, self.happiness, self.hunger, self.cuddle_level)

    def be_alive(self):
        super().be_alive()
        self.happiness += self.mopiness/2

    def cuddle(self, other_pet):
        for i in range(self.cuddle_level):
            other_pet.get_love()


cujo = Pet("Cujo")
benji = CuddlyPet("Benji")

print(cujo)
print(benji)

#print(cujo.happiness, cujo.fullness)
cujo.be_alive(5, 1)
#print(cujo.happiness, cujo.fullness)

#print(benji.happiness, benji.fullness)
benji.be_alive()
#print(benji.happiness, benji.fullness)
