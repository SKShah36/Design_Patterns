# The code example is adapted from https://sourcemaking.com/design_patterns/observer/python/1
# and https://www.geeksforgeeks.org/observer-pattern-set-1-introduction/

import abc
import math


class CricketData:
    """
    Know its observers. Any number of Observer objects may observe a
    subject.
    Send a notification to its observers when its state changes.
    """

    def __init__(self):
        self._observers = set()
        self._subject_state = None
        self._runs = 0
        self._wickets = 0
        self._overs = 0.1

    def attach(self, observer):
        observer._subject = self
        self._observers.add(observer)

    def detach(self, observer):
        observer._subject = None
        self._observers.discard(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update(self._runs, self._wickets, self._overs)

    @property
    def latest_runs(self) -> int:
        return self._runs

    @latest_runs.setter
    def latest_runs(self, runs):
        self._runs = runs
        self._notify()

    @property
    def latest_wickets(self) -> int:
        return self._wickets

    @latest_wickets.setter
    def latest_wickets(self, wickets):
        self._wickets = wickets
        self._notify()

    @property
    def latest_overs(self) -> float:
        return self._overs

    @latest_overs.setter
    def latest_overs(self, overs):
        self._overs = overs
        self._notify()


class Observer(metaclass=abc.ABCMeta):
    """
    Define an updating interface for objects that should be notified of
    changes in a subject.
    """

    def __init__(self):
        self._subject = None
        self._runs = None
        self._wickets = None
        self._overs = None

    @abc.abstractmethod
    def update(self, runs: int, wickets: int, overs: float):
        pass

    @abc.abstractmethod
    def _display(self):
        pass


class AverageScoreDisplay(Observer):
    """
    Implement the Observer updating interface to keep its state
    consistent with the subject's.
    Store state that should stay consistent with the subject's.
    """

    def __init__(self):
        super().__init__()
        self._run_rate = None
        self._predicted_score = None

    def update(self, runs: int, wickets: int, overs: float) -> None:
        self._runs = runs
        self._wickets = wickets
        self._overs = overs
        complete_overs = math.floor(overs)
        total_balls = complete_overs*6 + (self._overs - complete_overs)*10
        conv_overs = total_balls / 6
        self._run_rate = self._runs/conv_overs
        self._predicted_score = int(self._run_rate * 50)
        self._display()

    def _display(self):
        print("Current run rate: {}, Predicted score: {}".format(self._run_rate, self._predicted_score))


class CurrentScoreDisplay(Observer):
    """
    Implement the Observer updating interface to keep its state
    consistent with the subject's.
    Store state that should stay consistent with the subject's.
    """
    def __init__(self):
        super().__init__()

    def update(self, runs: int, wickets: int, overs: float) -> None:
        self._runs = runs
        self._wickets = wickets
        self._overs = overs
        self._display()

    def _display(self) -> None:
        print("Current score: {}, Current wickets: {}, Current overs: {}".format(self._runs, self._wickets,
                                                                                 self._overs))


def main():
    cric_data = CricketData()
    average_score_display = AverageScoreDisplay()
    current_score_display = CurrentScoreDisplay()

    cric_data.attach(average_score_display)
    cric_data.attach(current_score_display)

    cric_data.latest_overs = 1
    cric_data.latest_runs = 5


if __name__ == "__main__":
    main()