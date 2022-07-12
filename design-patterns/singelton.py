
from abc import abstractstaticmethod
from asyncio.log import logger


class Logger(object):
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
        
        return cls._instance


    def print_something(self):
        print("Something")


########### Another approach #################


class SingeltonPerson:
    _instance = None

    @staticmethod
    def get_instance():
        if not SingeltonPerson._instance:
            SingeltonPerson._instance = SingeltonPerson("John", "Doe")

        return SingeltonPerson._instance

    def __init__(self, firstName, lastName) -> None:
        if SingeltonPerson._instance:
            raise Exception("Cannot instantian a new Instance, Please use the static method get_instance")

        self.firstName = firstName
        self.lastName = lastName
        SingeltonPerson._instance = self

    def print_name(self):
        print(f"{self.firstName} {self.lastName}")

if __name__ == "__main__":
    # logger = Logger()
    # logger.print_something()
    # logger_two = Logger()
    # logger_two.print_something()
    # print(logger == logger_two)

    person = SingeltonPerson("Richard", "Pitt")
    person.print_name()
    #person2 = SingeltonPerson("asdf", "reerqa")
    person2 = SingeltonPerson.get_instance()
    person2.print_name()
    print(person == person2)

