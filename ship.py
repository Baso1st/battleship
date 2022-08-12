from abc import ABC

class Ship(ABC):
    def __init__(self, name, size):
        self.name = name
        self._size = size

    @property
    def size(self):
        return self._size

    def take_hit(self):
        self._size -= 1
        return self.get_hit_report()

    def __str__(self):
        return f"{type(self).__name__} {self.name}"

    def get_hit_report(self):
        if self._size > 0:
            return str(self) + f" is criticaly hit. Remaining health: {self._size}"
        else:
            return str(self) + f" has been destroyed"

class AirCraftCarrier(Ship):
    def __init__(self, name):
        super().__init__(name, 5)

class Destroyer(Ship):
    def __init__(self, name):
        super().__init__(name, 3)

class SmallBoat(Ship):
    def __init__(self, name):
        super().__init__(name, 1)

class Submarine(Ship):
    def __init__(self, name):
        super().__init__(name, 2)