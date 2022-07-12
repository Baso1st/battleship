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
        

class AnimalFactory:
    
    @staticmethod
    def get_animal(animalType):
        if animalType.upper() == "DOG":
            return Dog()
        if animalType.upper() == "CAT":
            return Cat()

if __name__ == "__main__":
    dog = AnimalFactory.get_animal("dog")
    cat = AnimalFactory.get_animal("cat")

    dog.make_sound()
    cat.make_sound()