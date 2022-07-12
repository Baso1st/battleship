from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def register(self, observer):
        pass

    @abstractmethod
    def unregister(self, observer):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self, newVal):
        pass

class WeatherSubject(Subject):
    def __init__(self) -> None:
        self.observers = set()

    def register(self, observer):
        self.observers.add(observer)

    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
        
    def notifyObservers(self, newVal):
        for obs in self.observers:
            obs.update(newVal)
    
    def weatherChange(self, weatherStatus):
        self.notifyObservers(weatherStatus)


class weatherObserver(Observer):

    observer_count = 0
    def __init__(self, subject) -> None:
        self.subject = subject
        self.subject.register(self)
        weatherObserver.observer_count += 1
        self.observer_id = weatherObserver.observer_count
    
    def update(self, newVal):
        print(f"New weather update from observer {self.observer_id}: {newVal}")





if __name__ == '__main__':
    weatherSubject = WeatherSubject()
    firstObserver = weatherObserver(weatherSubject)
    secondObserver = weatherObserver(weatherSubject)

    weatherSubject.weatherChange('Precip 98%, High: 78, Low: 35')
    weatherSubject.weatherChange('Precip 30%, High: 40, Low: 25')
