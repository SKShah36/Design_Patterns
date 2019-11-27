"""
This code is adapted from https://www.geeksforgeeks.org/decorator-pattern-set-3-coding-the-design/
"""

import abc


class Pizza:
    def __init__(self):
        self._description = "unknown pizza"

    def get_description(self) -> str:
        return self._description

    @abc.abstractmethod
    def get_cost(self) -> int:
        pass


class PeppyPaneer(Pizza):
    def __init__(self):
        super().__init__()
        self._description = "Peppy Paneer"

    def get_cost(self) -> int:
        return 100


class FarmHouse(Pizza):
    def __init__(self):
        super().__init__()
        self._description = "FarmHouse"

    def get_cost(self) -> int:
        return 200


class Margherita(Pizza):
    def __init__(self):
        super().__init__()
        self._description = "Margherita"

    def get_cost(self) -> int:
        return 100


class ChickenFiesta(Pizza):
    def __init__(self):
        super().__init__()
        self._description = "Chicken Fiesta"

    def get_cost(self) -> int:
        return 200


class SimplePizza(Pizza):
    def __init__(self):
        super().__init__()
        self._description = "Simple Pizza"

    def get_cost(self) -> int:
        return 50


class ToppingDecorator(Pizza):
    @abc.abstractmethod
    def get_description(self) -> str:
        pass


class FreshTomato(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__()
        self._pizza = pizza

    def get_description(self) -> str:
        return self._pizza.get_description() + ", Fresh Tomato"

    def get_cost(self) -> int:
        return self._pizza.get_cost() + 40


class Barbecue(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__()
        self._pizza = pizza

    def get_description(self) -> str:
        return self._pizza.get_description() + ", Barbeque"

    def get_cost(self) -> int:
        return self._pizza.get_cost() + 90


class Paneer(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__()
        self._pizza = pizza

    def get_description(self) -> str:
        return self._pizza.get_description() + ", Paneer"

    def get_cost(self) -> int:
        return self._pizza.get_cost() + 70


def driver():
    pizza1 = Margherita()
    print("{} Cost: {}".format(pizza1.get_description(), pizza1.get_cost()))

    pizza2 = FreshTomato(FarmHouse())
    print("{} Cost: {}".format(pizza2.get_description(), pizza2.get_cost()))

    pizza3 = Barbecue(pizza2)
    print("{} Cost: {}".format(pizza3.get_description(), pizza3.get_cost()))


if __name__ == "__main__":
    driver()


