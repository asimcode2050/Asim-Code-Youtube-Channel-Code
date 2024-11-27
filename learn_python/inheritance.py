class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print(f"The {self.species} named {self.name} makes a sound.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def speak(self):
        print(f"The dog named {self.name}, who is a {self.breed}, barks.")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color  # Specific attribute for Cat: color of the cat.

    def speak(self):
        print(f"The cat named {self.name}, who is {
              self.color} in color, meows.")


animal = Animal("Generic Animal", "Unknown")
animal.speak()  # Output: The Unknown named Generic Animal makes a sound.
dog = Dog("Buddy", "Golden Retriever")
dog.speak()
cat = Cat("Whiskers", "black")
cat.speak()
