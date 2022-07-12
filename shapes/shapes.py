from abc import ABC, abstractmethod

class Polygon(ABC):

    @abstractmethod
    def get_sides(self):
        pass


class Triangel(Polygon):

    def get_sides(self):
        return 3


class Rectangel(Polygon):

    def get_sides(self):
        return 4

class Square(Rectangel):
     
     def get_sides(self):
         return super().get_sides()



class TestShape:
    def print_shape_sides(self, shape: Polygon):
        if not isinstance(shape, Polygon):
            raise TypeError("shape must be a Polygon")
        print(f"{type(shape).__name__} number of sides: {shape.get_sides()}")
        
        


if __name__ == '__main__':
    #print("Entry player names: ")
    player_one, player_two = input("Entry player names: ").split()
    print(f"Welcome {player_one} and {player_two}")