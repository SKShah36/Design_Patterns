from abc import ABC, abstractmethod
from typing import Tuple

class HousePlan(ABC):
    @abstractmethod
    def set_basement(self, basement: str):
        pass

    def set_structure(self, structure: str):
        pass

    def set_roof(self, roof: str):
        pass

    def set_interior(self, interior: str):
        pass


class House(HousePlan):
    def __init__(self):
        self._basement = None
        self._structure = None
        self._roof = None
        self._interior = None

    def set_basement(self, basement: str):
        self._basement = basement

    def set_structure(self, structure: str):
        self._structure = structure

    def set_roof(self, roof: str):
        self._roof = roof

    def set_interior(self, interior: str):
        self._interior = interior


class HouseBuilder:
    def build_basement(self) -> None:
        pass

    def build_structure(self) -> None:
        pass

    def build_roof(self) -> None:
        pass

    def build_interior(self) -> None:
        pass

    def get_house(self) -> Tuple[House, str]:
        pass


class IglooBuilder(HouseBuilder):
    def __init__(self):
        self._house = House()

    def build_basement(self) -> None:
        self._house.set_basement("Ice Bars")

    def build_structure(self) -> None:
        self._house.set_structure("Ice Blocks")

    def build_roof(self) -> None:
        self._house.set_roof("Ice Dome")

    def build_interior(self) -> None:
        self._house.set_interior("Ice Carvings")

    def get_house(self) -> Tuple[House, str]:
        return self._house, self.__class__.__name__


class TipiHouseBuilder(HouseBuilder):
    def __init__(self):
        self._house = House()

    def build_basement(self) -> None:
        self._house.set_basement("Wooden Poles")

    def build_structure(self) -> None:
        self._house.set_structure("Wood and Ice")

    def build_roof(self) -> None:
        self._house.set_roof("Wood, caribou and seal skins")

    def build_interior(self) -> None:
        self._house.set_interior("Fire Wood")

    def get_house(self) -> Tuple[House, str]:
        return self._house, self.__class__.__name__


class Architect:
    def __init__(self, house_builder: HouseBuilder):
        self._house_builder = house_builder

    def get_house(self) -> Tuple[House, str]:
        return self._house_builder.get_house()

    def construct_house(self) -> None:
        self._house_builder.build_basement()
        self._house_builder.build_structure()
        self._house_builder.build_roof()
        self._house_builder.build_interior()


build_igloo = IglooBuilder()
architect = Architect(build_igloo)
architect.construct_house()
house = architect.get_house()

print("Architect has constructed house {} using {}".format(id(house), house[1]))










