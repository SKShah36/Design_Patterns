import abc
from typing import Final
from random import choice


class Player(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def assign_weapon(self, weapon: str) -> None:
        pass

    @abc.abstractmethod
    def mission(self) -> None:
        pass


class Terrorist(Player):
    def __init__(self):
        self._TASK: Final = "PLANT A BOMB"
        self._weapon = None

    def assign_weapon(self, weapon: str) -> None:
        self._weapon = weapon

    def mission(self) -> None:
        print("Terrorist with weapon {} | Task is {} ".format(self._weapon, self._TASK))


class CounterTerrorist(Player):
    def __init__(self):
        self._TASK: Final = "DIFFUSE BOMB"
        self._weapon = None

    def assign_weapon(self, weapon: str) -> None:
        self._weapon = weapon

    def mission(self) -> None:
        print("Counter Terrorist with weapon {} | Task is {} ".format(self._weapon, self._TASK))


class PlayerFactory:
    hm = {}

    @classmethod
    def get_player(cls, player_type: str):
        hm = PlayerFactory.hm
        p = None
        if player_type in hm:
            p = hm[player_type]
        else:
            if player_type == "Terrorist":
                print("Terrorist created")
                p = Terrorist()
            elif player_type == "CounterTerrorist":
                print("Counter Terrorist created")
                p = CounterTerrorist()

            hm[player_type] = p
        return p


def driver():
    player_type = ["Terrorist", "CounterTerrorist"]
    weapons = ["AK-47", "Maverick", "Gut Knife", "Desert Eagle"]

    for i in range(10):
        p = PlayerFactory.get_player(choice(player_type))
        p.assign_weapon(choice(weapons))
        p.mission()


if __name__ == "__main__":
    driver()


