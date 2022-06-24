class SimpleList:
    def __init__(self, items) -> None:
        self._items = list(items)

    
    def add(self, item):
        self._items.append(item)


    def sort(self):
        self._items.sort()


    def __get_item__(self, index):
        return self._items[index]
    

    def __len__(self):
        return len(self._items)


    def __repr__(self):
        return f"{type(self).__name__}({self._items!r})"
        

class SortedList(SimpleList):
    def __init__(self, items) -> None:
        super().__init__(items)
        self.sort()

    
    def add(self, item):
        super().add(item)
        self.sort()


class IntList(SimpleList):
    def __init__(self, items) -> None:
        for x in items: self._validate(x)
        super().__init__(items)

    @staticmethod
    def _validate(item):
        if not isinstance(item, int):
            raise TypeError("IntList only supports integer values")

    
    def add(self, item):
        self._validate(item)
        super().add(item)


class SortedIntList(IntList, SortedList):
    pass

if __name__ == '__main__':
    simple = SimpleList([3, 4, 5, 1])
    sortedList = SortedList([3, 4, 5, 1])
    intList = IntList([3, 4, 5, 1])
    sortedIntList = SortedIntList([3, 4, 5, 1])
    sortedIntList.add(2)
    print(simple)
    print(sortedList)
    print(intList)
    print(sortedIntList)