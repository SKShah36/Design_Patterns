# This code is written using references from https://refactoring.guru/design-patterns/abstract-factory and
# https://refactoring.guru/design-patterns/abstract-factory/python/example

import abc
from abc import abstractmethod


class Chair(metaclass=abc.ABCMeta):
    @abstractmethod
    def has_seat_type(self) -> str:
        pass

    @abstractmethod
    def price(self) -> int:
        pass


class Coffee_Table(metaclass=abc.ABCMeta):
    @abstractmethod
    def has_wood_type(self) -> str:
        pass

    @abstractmethod
    def price(self) -> int:
        pass


class Sofa(metaclass=abc.ABCMeta):
    @abstractmethod
    def has_seat_type(self) -> str:
        pass

    @abstractmethod
    def price(self) -> int:
        pass


class VictorianChair(Chair):
    def has_seat_type(self) -> str:
        return "Soft Red Velvet"

    def price(self) -> int:
        return 5000


class VictorianCoffeeTable(Coffee_Table):
    def has_wood_type(self) -> str:
        return "Victorian wood"

    def price(self) -> int:
        return 10000


class VictorianSofa(Sofa):
    def has_seat_type(self) -> str:
        return "Victorian Suede"

    def price(self) -> int:
        return 100000


class ModernChair(Chair):
    def has_seat_type(self) -> str:
        return "Modern Blue"

    def price(self) -> int:
        return 2500


class ModernCoffeeTable(Coffee_Table):
    def has_wood_type(self) -> str:
        return "Synthetic Ply"

    def price(self) -> int:
        return 7800


class ModernSofa(Sofa):
    def has_seat_type(self) -> str:
        return "Modern seat for modern sofa"

    def price(self) -> int:
        return 80000


class FurnitureFactory(metaclass=abc.ABCMeta):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_coffee_table(self) -> Coffee_Table:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> VictorianChair:
        return VictorianChair()

    def create_coffee_table(self) -> VictorianCoffeeTable:
        return VictorianCoffeeTable()

    def create_sofa(self) -> VictorianSofa:
        return VictorianSofa()


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> ModernChair:
        return ModernChair()

    def create_coffee_table(self) -> ModernCoffeeTable:
        return ModernCoffeeTable()

    def create_sofa(self) -> ModernSofa:
        return ModernSofa()


def client_code(furniture_factory: FurnitureFactory) -> None:
    chair = furniture_factory.create_chair()
    coffee_table = furniture_factory.create_coffee_table()
    sofa = furniture_factory.create_sofa()

    print("Chair Model: {}\nSeat type: {} \nPrice: {}".format(chair.__class__.__name__, chair.has_seat_type(), chair.
                                                              price()))
    print("Coffee table Model: {}\nWood type: {} \nPrice: {}".format(coffee_table.__class__.__name__, coffee_table.
                                                                     has_wood_type(), coffee_table.price()))
    print("Sofa Model: {}\nSeat type: {} \nPrice: {}".format(sofa.__class__.__name__, sofa.has_seat_type(),
                                                             sofa.price()))


if __name__ == "__main__":
    print("Client: Testing code with VictorianFurnitureFactory")
    client_code(VictorianFurnitureFactory())

    print("\n")

    print("Client: Testing code with VictorianFurnitureFactory")
    client_code(ModernFurnitureFactory())
