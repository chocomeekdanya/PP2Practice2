class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        super().speak()   # call parent method
        print("Dog barks")


d = Dog()
d.speak()
