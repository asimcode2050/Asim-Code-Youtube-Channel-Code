class Animal:
    def speak(self):
        print("The animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("The dog barks")


class Cat(Animal):
    def speak(self):
        print("The cat meows")


def make_animal_speak(animal):
    animal.speak()


dog = Dog()
cat = Cat()  # Create an instance (object) of the Cat class
make_animal_speak(dog)
make_animal_speak(cat)
