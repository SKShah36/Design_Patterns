# This code is adapted from https://www.geeksforgeeks.org/template-method-design-pattern/

import abc
from abc import abstractmethod


class OrderProcessTemplate(metaclass=abc.ABCMeta):
    isGift: bool

    @abstractmethod
    def do_select(self)->None:
        pass

    @abstractmethod
    def do_payment(self) -> None:
        pass

    # Do not override
    def gift_wrap(self) -> None:
        print("Gift wrap successful")

    @abstractmethod
    def do_delivery(self) -> None:
        pass

    # Do not override
    def process_order(self, is_gift: bool):
        self.do_select()
        self.do_payment()
        if is_gift:
            self.gift_wrap()
        self.do_delivery()


class NetOrder(OrderProcessTemplate):
    def do_select(self) ->None:
        print("Item added to online shopping cart")
        print("Get gift wrap preference")
        print("Get delivery address.")

    def do_payment(self) -> None:
        print("Online Payment through Netbanking, card or Paytm")

    def do_delivery(self) -> None:
        print("Ship the item through post to delivery address")


class StoreOrder(OrderProcessTemplate):
    def do_select(self) ->None:
        print("Customer chooses the item from shelf.")

    def do_payment(self) -> None:
        print("Pays at counter through cash/POS")

    def do_delivery(self) -> None:
        print("Item deliverd to in delivery counter.")


def client():
    net_order = NetOrder()
    net_order.process_order(True)
    print("")
    store_order = StoreOrder()
    store_order.process_order(True)


client()

