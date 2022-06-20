
class ShippingContainer:
    
    next_serial = 1337

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result


    def __init__(self, owner_code, content):
        self.owner_code = owner_code
        self.content = content
        self.serial = ShippingContainer._generate_serial()




if __name__ == '__main__':
     c6 = ShippingContainer('YML', ['Books'])
     print(c6.serial)
     print(ShippingContainer.next_serial)