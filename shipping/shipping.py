
import iso6346
class ShippingContainer:
    
    next_serial = 1337

    @staticmethod
    def _create_bic_code(owner_code, serial):
        return iso6346.create(owner_code, serial = str(serial).zfill(6)) 


    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result


    @classmethod
    def create_empty(cls, owner_code, **kwargs):
        return cls(owner_code, content=[], **kwargs)


    @classmethod
    def create_with_items(cls, owner_code, items, **kwargs):
        return cls(owner_code, content = list(items), **kwargs)


    def __init__(self, owner_code, content, **kwargs):
        self.owner_code = owner_code
        self.content = content
        self.bic = self._create_bic_code(owner_code, ShippingContainer._generate_serial())

class RefrigratedShippingContainer(ShippingContainer):

    MAX_celsius = 4

    def __init__(self, owner_code, content, *, celsius, **kwargs):
        super().__init__(owner_code, content, **kwargs)
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value > RefrigratedShippingContainer.MAX_celsius:
            raise ValueError("Temperature too hot")
        self._celsius = value
    

    @property
    def fahrenheite(self):
        return RefrigratedShippingContainer._c_to_f(self.celsius)

    @fahrenheite.setter
    def fahrenheite(self, value):
        self.celsius = RefrigratedShippingContainer._f_to_c(value)


    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32


    @staticmethod
    def _f_to_c(fahrenheite):
        return (fahrenheite - 32) * 5/9


    @staticmethod
    def _create_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code = owner_code,
            serial = str(serial).zfill(6),
            category = 'R'
            )


if __name__ == '__main__':
    c = RefrigratedShippingContainer.create_empty('MHE', celsius = 3)
    # c = RefrigratedShippingContainer.create_with_items('MHE', ['Onions'], celsius = 2)
    c.fahrenheite = 32
    print(c.bic)
    print(c.celsius)
    print(c.fahrenheite)