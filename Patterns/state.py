# The code is adapted from Derek Banas' Design Pattern tutorial available at
# https://www.newthinktank.com/2012/10/state-design-pattern-tutorial/

import abc


class ATMState(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert_card(self):
        pass

    @abc.abstractmethod
    def eject_card(self):
        pass

    @abc.abstractmethod
    def insert_pin(self, pin_entered: int):
        pass

    @abc.abstractmethod
    def request_cash(self, cash_to_withdraw: int):
        pass


class ATMMachine:
    def __init__(self):
        self._has_card = HasCard(self)
        self._no_card = NoCard(self)
        self._has_correct_pin = HasPin(self)
        self._atm_empty = NoCash(self)
        self._atmState = self._no_card
        self._cash_in_machine = 2000
        self._correct_pin_entered = False

        if self._cash_in_machine < 0:
            self._atmState = self._atm_empty

    def set_atm_state(self, atm_state: ATMState) -> None:
        self._atmState = atm_state

    def set_cash_in_machine(self, cash: int) -> None:
        self._cash_in_machine = cash

    def insert_card(self) -> None:
        self._atmState.insert_card()

    def eject_card(self) -> None:
        self._atmState.eject_card()

    def request_cash(self, cash_to_withdraw: int) -> None:
        self._atmState.request_cash(cash_to_withdraw)

    def insert_pin(self, pin_entered: int) -> None:
        self._atmState.insert_pin(pin_entered)

    def get_yes_card_state(self) -> ATMState:
        return self._has_card

    def get_no_card_state(self) -> ATMState:
        return self._no_card

    def get_has_pin(self) -> ATMState:
        return self._has_correct_pin

    def get_no_cash_state(self) -> ATMState:
        return self._atm_empty


class HasCard(ATMState):
    def __init__(self, atm_machine):
        self._atm_machine = atm_machine

    def insert_card(self) -> None:
        print("You can only insert one card at a time")

    def eject_card(self) -> None:
        print("Your card is ejected")
        self._atm_machine.set_atm_state(self._atm_machine.get_no_card_state())

    def request_cash(self, cash_to_withdraw: int) -> None:
        print("You have not entered your PIN")

    def insert_pin(self, pin_entered: int) -> None:
        atm_machine = self._atm_machine
        if pin_entered == 1234:
            print("You entered the correct pin")
            atm_machine._correct_pin_entered = True
            atm_machine.set_atm_state(atm_machine.get_has_pin())

        else:
            print("You entered the wrong pin")
            atm_machine._correct_pin_entered = False
            print("Your card is ejected")
            atm_machine.set_atm_state(atm_machine.get_no_card_state())


class NoCard(ATMState):
    def __init__(self, atm_machine):
        self._atm_machine = atm_machine

    def insert_card(self) -> None:
        print("Please enter your PIN")
        self._atm_machine.set_atm_state(self._atm_machine.get_yes_card_state())

    def eject_card(self) -> None:
        print("You didn't enter a card")

    def request_cash(self, cash_to_withdraw: int) -> None:
        print("You have not entered your card")

    def insert_pin(self, pin_entered: int) -> None:
        print("You have not entered your card")


class HasPin(ATMState):
    def __init__(self, atm_machine):
        self._atm_machine = atm_machine

    def insert_card(self) -> None:
        print("You have already entered a card")

    def eject_card(self) -> None:
        print("Your card is ejected")
        self._atm_machine.set_atm_state(self._atm_machine.get_no_card_state())

    def request_cash(self, cash_to_withdraw: int) -> None:
        atm_machine = self._atm_machine
        if cash_to_withdraw > atm_machine._cash_in_machine:
            print("You don't have that much case available")
            print("Your card is ejected")
            atm_machine.set_atm_state(atm_machine.get_no_card_state())

        else:
            print("{} is provided by the machine".format(cash_to_withdraw))
            atm_machine.set_cash_in_machine(atm_machine._cash_in_machine - cash_to_withdraw)
            print("Your card is ejected")
            atm_machine.set_atm_state(atm_machine.get_no_card_state())

            if atm_machine._cash_in_machine <= 0:
                atm_machine.set_atm_state(atm_machine.get_no_cash_state())

    def insert_pin(self, pin_entered: int) -> None:
        print("You already entered a PIN")


class NoCash(ATMState):
    def __init__(self, atm_machine):
        self._atm_machine = atm_machine

    def insert_card(self) -> None:
        print("We don't have any money")
        print("Your card is ejected")

    def eject_card(self) -> None:
        print("We don't have any money")
        print("There is no card to eject")

    def request_cash(self, cash_to_withdraw: int) -> None:
        print("We don't have any money")

    def insert_pin(self, pin_entered: int) -> None:
        print("We don't have any money")


def main():
    atm_machine = ATMMachine()
    atm_machine.insert_card()
    atm_machine.eject_card()
    atm_machine.insert_card()
    atm_machine.insert_pin(1234)
    atm_machine.request_cash(2000)
    atm_machine.insert_card()
    atm_machine.insert_pin(1234)


if __name__ == "__main__":
    main()