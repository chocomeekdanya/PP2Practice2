class Animal:
    def eat(self):
        print("Animal is eating")


class Flyer:
    def fly(self):
        print("Flying in the sky")


class Swimmer:
    def swim(self):
        print("Swimming in water")


# Multiple inheritance
class Duck(Animal, Flyer, Swimmer):
    def sound(self):
        print("Quack!")


d = Duck()

d.eat()    # from Animal
d.fly()    # from Flyer
d.swim()   # from Swimmer
d.sound()  # from Duck
