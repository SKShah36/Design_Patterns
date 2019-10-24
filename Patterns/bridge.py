# Adapted from https://www.geeksforgeeks.org/bridge-design-pattern/

from abc import ABC, abstractmethod


# Abstraction Abstract Class
class Vehicle(ABC):
    def __init__(self, workshop1, workshop2):
        self.workshop1 = workshop1
        self.workshop2 = workshop2

    @abstractmethod
    def manufacture(self):
        pass


# Refined Abstraction - Class 1
class Car(Vehicle):
    def __init__(self, workshop1, workshop2):
        super().__init__(workshop1, workshop2)
        self.workshop1 = workshop1
        self.workshop2 = workshop2

    def manufacture(self):
        print("Car", end=" ")
        self.workshop1.work()
        self.workshop2.work()


# Refined Abstraction - Class 2
class Bike(Vehicle):
    def __init__(self, workshop1, workshop2):
        super().__init__(workshop1, workshop2)
        self.workshop1 = workshop1
        self.workshop2 = workshop2

    def manufacture(self):
        print("Bike", end=" ")
        self.workshop1.work()
        self.workshop2.work()


# Implementor Class
class Workshop(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def work(self):
        pass


# Concrete implementation - Class 1
class Produce(Workshop):
    def work(self):
        print("Produced", end=" ")


# Concrete implementation - Class 2
class Assemble(Workshop):
    def work(self):
        print("and assembled")


vehicle1 = Car(Produce(), Assemble())
vehicle1.manufacture()

vehicle2 = Bike(Produce(), Assemble())
vehicle2.manufacture()
