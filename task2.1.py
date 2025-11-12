class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} ест")
    def sleep(self):
        print(f"{self.name} спит")
    def make_sound(self):
        print(f"{self.name} издает звук")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def make_sound(self):
        print(f"{self.name} гавкает: Гав-гав!")

my_dog = Dog("Бобик", 3, "Лабрадор")
print(f"Имя: {my_dog.name}")
print(f"Возраст: {my_dog.age} года")
print(f"Порода: {my_dog.breed}")

my_dog.eat()
my_dog.sleep()
my_dog.make_sound()
