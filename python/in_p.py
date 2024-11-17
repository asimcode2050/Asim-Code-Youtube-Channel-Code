class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic animal sound"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        return "Bark!"


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def make_sound(self):
        return "Meow!"


dog = Dog("Buddy", "Golden Retriever")
print(f"{dog.name} says: {dog.make_sound()}")
cat = Cat("Whiskers", "Black")
print(f"{cat.name} says: {cat.make_sound()}")
