from abc import ABC, abstractmethod
from dis import dis

class Processor(ABC):
    @abstractmethod
    def perfrom_ops(self):
        pass

class Disk(ABC):
    @abstractmethod
    def store_data(self):
        pass

class Ram(ABC):
    @abstractmethod
    def store_temp_data(self):
        pass

class FourCoreProcessor(Processor):
    def perfrom_ops(self):
        print("Performing fast ops")

class OneCoreProcessor(Processor):
    def perfrom_ops(self):
        print("Performing one op at a time")

class slowRam(Ram):
    def store_temp_data(self):
        print("Slow store temp data, slow access temp data")

class FastRam(Ram):
    def store_temp_data(self):
        print("Fast store temp data, Fast access temp data")

class HDD(Disk):
    def store_data(self):
        print("Storing data slowly")

class SSD(Disk):
    def store_data(self):
        print("Storing data Fast")


class MachineFactory(ABC):
    @abstractmethod
    def get_processor(self):
        pass

    @abstractmethod
    def get_ram(self):
        pass

    @abstractmethod
    def get_disk(self):
        pass


class FastMachine(MachineFactory):
    def get_processor(self):
        return FourCoreProcessor()
    
    def get_ram(self):
        return FastRam()

    def get_disk(self):
        return SSD()

class SlowMachine(MachineFactory):
    def get_processor(self):
        return OneCoreProcessor()
    
    def get_ram(self):
        return slowRam()

    def get_disk(self):
        return HDD()


class MidRangeMachine(MachineFactory):
    def get_processor(self):
        return FourCoreProcessor()
    
    def get_ram(self):
        return slowRam()

    def get_disk(self):
        return HDD()


class ComputerDesigner():
    def __init__(self, machine: MachineFactory) -> None:
        self._machine = machine

    def test_run_machine(self):
        cpu = self._machine.get_processor()
        ram = self._machine.get_ram()
        disk = self._machine.get_disk()

        cpu.perfrom_ops()
        ram.store_temp_data()
        disk.store_data()
        


if __name__ == "__main__":
    machines = [FastMachine(), SlowMachine(), MidRangeMachine()]
    for machine in machines:
        print(type(machine).__name__)
        designer = ComputerDesigner(machine)
        designer.test_run_machine()
        print('-'*50)
    
