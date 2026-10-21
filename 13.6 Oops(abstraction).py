# Abstraction

'''
Abstraction means hiding the implementation detials and showing only the functionality
to the user.

Python achieves abstraction primarily through Abstract Base Class (ABC),
provided by the abc module.

An abstarct class cannot be instantiated directly and serves as a template for other
classes

It can contain both concrete methods (With implmentation), and abstract methods
(Without implementation) 

Abstract method are declared using the @ abstarct method decorated.'''

from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
    def refuel(self):
        print('Refuelling the vehicle')

class Car(Vehicle):
    def start_engine(self):
        print('Car engine started with a key')
    def stop_engine(self):
        print('Car engine stopped')

class Motorcycle(Vehicle):
    def start_engine(self):
        print('Bike engine started with a key')
    def stop_engine(self):
        print('Bike engine stopped')

mycar = Car()
mycar.start_engine()
mycar.stop_engine()
mycar.refuel()

mybike = Motorcycle()
mybike.start_engine()
mybike.stop_engine()
mybike.refuel()



