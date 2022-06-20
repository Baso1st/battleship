
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

    MAX_CELSIOUS = 4

    def __init__(self, owner_code, content, *, celsious, **kwargs):
        super().__init__(owner_code, content, **kwargs)
        if celsious > RefrigratedShippingContainer.MAX_CELSIOUS:
            raise ValueError("Temperature too hot")
        self.celsious = celsious

    @staticmethod
    def _create_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code = owner_code,
            serial = str(serial).zfill(6),
            category = 'R'
            )


if __name__ == '__main__':
    c = RefrigratedShippingContainer.create_empty('MHE', celsious = 3)
    # c = RefrigratedShippingContainer.create_with_items('MHE', ['Onions'], celsious = 2)
    print(c.bic)
    print(c.celsious)