class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog:
    def bark(self):
        print("Dog barks")


class Pet(Animal, Dog):
    def play(self):
        print("Pet is playing")


pet = Pet()  # pet is now an instance of the Pet class
pet.speak()  # Output: Animal makes a sound
pet.bark()  # Output: Dog barks
pet.play()  # Output: Pet is playing
