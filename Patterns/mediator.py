# The mediator object: encapsulates all interconnections, acts as the hub of communication, is responsible for
# controlling and coordinating the interactions of its clients, and promotes loose coupling by keeping objects from
# referring to each other explicitly.

from __future__ import annotations
import abc

class Command(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def land(self) -> None:
        pass


class IATCMediator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def register_runway(self, runway: Runway) -> None:
        pass

    @abc.abstractmethod
    def register_flight(self, flight: Flight) -> None:
        pass

    @abc.abstractmethod
    def is_landing_ok(self) -> bool:
        pass

    @abc.abstractmethod
    def set_landing_status(self, status: bool) -> None:
        pass


class ATCMediator(IATCMediator):
    def __init__(self):
        self._flight = None
        self._runway = None
        self._land = None

    def register_runway(self, runway: Runway) -> None:
        self._runway = runway

    def register_flight(self, flight: Flight) -> None:
        self._flight = flight

    def is_landing_ok(self) -> bool:
        return self._land

    def set_landing_status(self, status: bool) -> None:
        self._land = status


class Flight(Command):
    def __init__(self, atc_mediator):
        self._atc_mediator = atc_mediator

    def land(self) -> None:
        if self._atc_mediator.is_landing_ok():
            print("Successfully landed")
            self._atc_mediator.set_landing_status(True)
        else:
            print("Waiting for landing")

    def get_ready(self) -> None:
        print("Ready for landing")


class Runway(Command):
    def __init__(self, atc_mediator):
        self._atc_mediator = atc_mediator

    def land(self) -> None:
        print("Landing permission granted")
        self._atc_mediator.set_landing_status(True)


def client():
    atc_mediator = ATCMediator()
    sparrow101 = Flight(atc_mediator)
    main_runway = Runway(atc_mediator)
    atc_mediator.register_flight(sparrow101)
    atc_mediator.register_runway(main_runway)
    sparrow101.get_ready()
    main_runway.land()
    sparrow101.land()


if __name__ == "__main__":
    client()