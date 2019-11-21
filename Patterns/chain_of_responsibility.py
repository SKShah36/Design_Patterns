# This code is adpated from https://www.geeksforgeeks.org/chain-responsibility-design-pattern/

from __future__ import annotations
import abc


class Chain(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def set_next(self, next_in_chain: Chain) -> None:
        pass

    @abc.abstractmethod
    def process(self, request: Number) -> None:
        pass


class Number:
    def __init__(self, number: int):
        self._number = number

    def get_number(self):
        return self._number


class NegativeProcessor(Chain):
    def __init__(self):
        self._next_in_chain = None

    def set_next(self, c: Chain) -> None:
        self._next_in_chain = c

    def process(self, request: Number) -> None:
        if request.get_number() < 0:
            print("Negative Processor: {}".format(request.get_number()))
        else:
            self._next_in_chain.process(request)


class ZeroProcessor(Chain):
    def __init__(self):
        self._next_in_chain = None

    def set_next(self, c: Chain) -> None:
        self._next_in_chain = c

    def process(self, request: Number) -> None:
        if request.get_number() == 0:
            print("Zero Processor: {}".format(request.get_number()))
        else:
            self._next_in_chain.process(request)


class PositiveProcessor(Chain):
    def __init__(self):
        self._next_in_chain = None

    def set_next(self, c: Chain) -> None:
        self._next_in_chain = c

    def process(self, request: Number) -> None:
        if request.get_number() > 0:
            print("Positive Processor: {}".format(request.get_number()))
        else:
            self._next_in_chain.process(request)


def client():
    c1 = NegativeProcessor()
    c2 = ZeroProcessor()
    c3 = PositiveProcessor()
    c1.set_next(c2)
    c2.set_next(c3)

    c1.process(Number(90))
    c1.process(Number(-50))
    c1.process(Number(0))
    c1.process(Number(91))


if __name__ == "__main__":
    client()

