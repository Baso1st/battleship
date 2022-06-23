
import iso6346
class ShippingContainer:
    
    next_serial = 1337
    HEIGHT_FT = 8.5
    WIDTH_FT = 8


    @property
    def volum(self):
        return self._calc_volum()

    def _calc_volum(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code, serial = str(serial).zfill(6)) 

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result


    @classmethod
    def create_empty(cls, owner_code, length_ft, **kwargs):
        return cls(owner_code, length_ft, content=[], **kwargs)


    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, **kwargs):
        return cls(owner_code, length_ft, content = list(items), **kwargs)


    def __init__(self, owner_code, length_ft, content, **kwargs):
        self.owner_code = owner_code
        self.length_ft = length_ft
        self.content = content
        self.bic = self._make_bic_code(owner_code, serial = ShippingContainer._generate_serial())

    def __init__(self, owner_code, length_ft, content, **kwargs):
        self.owner_code = owner_code
        self.length_ft = length_ft
        self.contents = content

class RefrigeratedShippingContainer(ShippingContainer):

    MAX_celsius = 4
    FRIDGE_VOLUM_FT3 = 100

    def __init__(self, owner_code, length_ft, content, *, celsius, **kwargs):
        super().__init__(owner_code, length_ft, content, **kwargs)
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._set_celsius(value)

    def _set_celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_celsius:
            raise ValueError("Temperature too hot")
        self._celsius = value


    @property
    def fahrenheite(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)

    @fahrenheite.setter
    def fahrenheite(self, value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)


    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32


    @staticmethod
    def _f_to_c(fahrenheite):
        return (fahrenheite - 32) * 5/9

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code = owner_code,
            serial = str(serial).zfill(6),
            category = 'R'
            )


    def _calc_volum(self):
     return super()._calc_volum() - RefrigeratedShippingContainer.FRIDGE_VOLUM_FT3


class HeatedRefrigeratedContainer(RefrigeratedShippingContainer):
    MIN_CELSIUS = -20

    def _set_celsius(self, value):
        if value < HeatedRefrigeratedContainer.MIN_CELSIUS:
            raise ValueError("Temperature Too Cold")
        return super()._set_celsius(value)


if __name__ == '__main__':
    c = ShippingContainer.create_empty('MHE', length_ft = 20, celsius = 3)
    c2 = RefrigeratedShippingContainer.create_empty("ABC", length_ft = 20, celsius = 2)
    c3 = HeatedRefrigeratedContainer.create_empty("DEF", length_ft = 20, celsius = -14)
    print(c.volum)
    print(c2.volum)