from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):

    def make_sound(self):
        print("Bark")


class Cat(Animal):

    def make_sound(self):
        print("Meow")


class AnimalFactory(ABC):

    def get_animal(self):
        return self.create_animal()

    @abstractmethod
    def create_animal(self):
        pass


class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()
        

if __name__ == "__main__":
    dogFactory = DogFactory()
    dog = dogFactory.get_animal()
    catFactory = CatFactory()
    cat = catFactory.get_animal()

    dog.make_sound()
    cat.make_sound()