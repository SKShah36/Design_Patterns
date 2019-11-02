from abc import ABC, abstractmethod


class ShoppingCartVisitor(ABC):
    def visit(self, obj):
        pass


class ItemElement(ABC):
    def accept(self, visitor: ShoppingCartVisitor) -> None:
        pass


class Book(ItemElement):
    def __init__(self, cost: int, isbn: str):
        self._price = cost
        self._isbnNumber = isbn

    def get_price(self) -> int:
        return self._price

    def get_isbn_number(self) -> str:
        return self._isbnNumber

    def accept(self, visitor: ShoppingCartVisitor):
        return visitor.visit(self)


class Fruit(ItemElement):
    def __init__(self, price_kg: int, wt: int, nm: str):
        self._price_kg = price_kg
        self._weight = wt
        self._name = nm

    def get_price_kg(self) -> int:
        return self._price_kg

    def get_weight(self) -> int:
        return self._weight

    def get_name(self) -> str:
        return self._name

    def accept(self, visitor: ShoppingCartVisitor):
        return visitor.visit(self)


class ShoppingCartVisitorImpl(ShoppingCartVisitor):
    def visit(self, obj) -> int:
        if isinstance(obj, Book):
            if obj.get_price() > 50:
                cost = obj.get_price() - 5
            else:
                cost = obj.get_price()

            print("Book ISBN::{} Cost = {}".format(obj.get_isbn_number(), cost))
            return cost

        elif isinstance(obj, Fruit):
            cost = obj.get_price_kg() + obj.get_weight()
            print("{}: {}".format(obj.get_name(), cost))
            return cost


def calculate_price(items: list) -> int:
    """

    :type items: list
    """
    visitor = ShoppingCartVisitorImpl()
    add = 0
    for item in items:
        add = add + item.accept(visitor)

    return add


items = [Book(20, "1234"), Book(100, "5678"), Fruit(10, 2, "Banana"), Fruit(5, 5, "Apple")]
total = calculate_price(items)
print("Total Cost: {}".format(total))
