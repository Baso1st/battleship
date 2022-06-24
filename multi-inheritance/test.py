
class Base:
    def __init__(self):
        print('Base Init')

    def f(self):
        print('Base f')


class Sub(Base):
    def __init__(self):
        super().__init__()

    
if __name__ == '__main__':
    print(f"{[1, 2, 3]!r}")