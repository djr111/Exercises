class Animal:
    def __init__(self):
        self.legs = 4
        self.noise = "null"

    class Amphibian:
        def __init__(self):
            self.breath = "Underwater"

    class Mammal:
        def __init__(self):

            self.breath = "Air"

class Avian(Animal):
    def __init__(self):
        super().__init__()
        self.noise = "chirp"

frog = Animal.Amphibian()
dog = Animal.Mammal()
Bird = Avian()

print(Bird.noise)

