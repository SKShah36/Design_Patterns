from abc import ABC, abstractmethod


class Expression:
    @abstractmethod
    def interpret(self, context):
        pass


class TerminalExpression(Expression):
    def __init__(self, data):
        self._data = data

    def interpret(self, context):
        return self._data in context


class OrExpression(Expression):
    def __init__(self, expr1, expr2):
        self._expr1 = expr1
        self._expr2 = expr2

    def interpret(self, context):
        return self._expr1.interpret(context) or self._expr2.interpret(context)


class AndExpression(Expression):
    def __init__(self, expr1, expr2):
        self._expr1 = expr1
        self._expr2 = expr2

    def interpret(self, context):
        return self._expr1.interpret(context) and self._expr2.interpret(context)


person1 = TerminalExpression("Ricky Ponting")
person2 = TerminalExpression("Brett Lee")
isSingle = OrExpression(person1, person2)

another_person = TerminalExpression("Sachin Tendulkar")
another_person_committed = TerminalExpression("Committed")
is_committed = AndExpression(another_person, another_person_committed)

isSingle.interpret("Ricky Ponting")
isSingle.interpret("Brett Lee")
isSingle.interpret("Warne")

is_committed.interpret("Committed, Sachin Tendulkar")
is_committed.interpret("Single, Sachin Tendulkar")