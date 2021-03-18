#https://www.youtube.com/watch?v=z_eALBTtQTk&ab_channel=AsimCode
class Dog():
    def __init__(self, name):
        self.name = name
    def sit(self):
        print(f"{self.name} is sitting.")
my_dog = Dog('Max')
#print(f"Name: {my_dog.name}")
#my_dog.sit()
class GoodDog(Dog):
    def __init__(self,name):
        super().__init__(name)
    def bark(self):
        print("wuff wuff")
good_boy = GoodDog('Buddy')
print(f"{good_boy.name} is a good boy")
good_boy.sit()
good_boy.bark()
