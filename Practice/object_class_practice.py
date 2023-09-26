class pet:
    name = ""
    age = 0
    animal = ""
    def __init__(self, name, age, animal):
        self.name = name
        self.age = age
        self.animal = animal

    def says(self):
        print(f"{self.name} is a {self.animal}")

    def calc(self):
        if self.age > 5:
            print(f"this {self.animal} is old.")
        else:
            print(f"this {self.animal} is young.")


class dog(pet):
    species = ""

    def __init__(self, name, age, animal, species):
        super().__init__(name, age, animal)
        self.species = species

    def bark(self):
        print(f"{self.name} is a {self.species}.\n{self.name} the {self.animal}, is barking")


spot = dog("spot", 6, "dog", "pomenarian")
bunny = pet("hopper", 3, "rabbit")

spot.bark()
spot.says()
bunny.says()