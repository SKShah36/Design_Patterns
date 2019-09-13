from abc import ABC, abstractmethod

class TextView:
    def get_extent(self):
        print("This is the specific request called get extent")


class Manipulator:
    @abstractmethod
    def manipulate(self):
        pass


class LineManipulator(Manipulator):
    def manipulate(self):
        print("I manipulate objects of line")


class TextManipulator(Manipulator):
    def manipulate(self):
        print("I manipulate objects of text")


# Abstract base class called Shape
class Shape(ABC):
    @abstractmethod
    def BoundingBox(self):
        pass

    @abstractmethod
    def CreateManipulator(self):
        pass


class Line(Shape):

    def __init__(self, manipulator):
        self.manipulate = manipulator

    def BoundingBox(self):
        print("This is the bounding box of {}".format(__class__.__name__))

    def CreateManipulator(self):
        return self.manipulate()


# This is the adapter class in the adapter pattern
class TextShape(Shape):
    def __init__(self, textview, manipulator):
        self.adaptee = textview
        self.manipulate = manipulator

    def BoundingBox(self):
        return self.adaptee.get_extent()

    # This functionality is not provided by adaptee but the adaptor class takes care of that
    def CreateManipulator(self):
        return self.manipulate()


def client_code(target):
    print("I am the client code. I do not understand interface of TextView. I know what TextShape does. I will call "
          "bounding box method of TextShape")

    print("Calling the bounding box method")
    target.BoundingBox()

    print("Creating a manipulator object")
    manipulated_obj = target.CreateManipulator()

    print("Calling manipulated object's manipulate method")
    manipulated_obj.manipulate()


if __name__ == "__main__":
    adaptee = TextView()
    adapter = TextShape(adaptee, TextManipulator)
    client_code(adapter)
