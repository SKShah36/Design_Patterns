import abc


class KickBehavior(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def kick(self):
        pass


class JumpBehavior(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def jump(self):
        pass


class Fighter(metaclass=abc.ABCMeta):
    def __init__(self, jump_behavior: JumpBehavior, kick_behavior: KickBehavior):
        self._jump_behavior = jump_behavior
        self._kick_behavior = kick_behavior

    def punch(self) -> None:
        print("Default punch")

    # @abc.abstractmethod
    def kick(self) -> None:
        self._kick_behavior.kick()

    # @abc.abstractmethod
    def jump(self) -> None:
        self._jump_behavior.jump()

    def roll(self) -> None:
        print("Default roll")

    def set_kick_behavior(self, kick_behavior: KickBehavior) -> None:
        self._kick_behavior = kick_behavior

    def set_jump_behavior(self, jump_behavior: JumpBehavior) -> None:
        self._jump_behavior = jump_behavior

    @abc.abstractmethod
    def display(self):
        pass


class LightningKick(KickBehavior):
    def kick(self):
        print("Lightning kick")


class TornadoKick(KickBehavior):
    def kick(self):
        print("Tornado kick")


class ShortJump(JumpBehavior):
    def jump(self):
        print("Short jump")


class LongJump(JumpBehavior):
    def jump(self):
        print("Long jump")


class Ramesh(Fighter):
    def __init__(self, jump_behavior: JumpBehavior, kick_behavior: KickBehavior):
        super().__init__(jump_behavior, kick_behavior)

    def display(self):
        print("I am {}".format(self.__class__.__name__))


class Suresh(Fighter):
    def __init__(self, jump_behavior: JumpBehavior, kick_behavior: KickBehavior):
        super().__init__(jump_behavior, kick_behavior)

    def display(self):
        print("I am {}".format(self.__class__.__name__))


class Mukesh(Fighter):
    def __init__(self, jump_behavior: JumpBehavior, kick_behavior: KickBehavior):
        super().__init__(jump_behavior, kick_behavior)

    def display(self):
        print("I am {}".format(self.__class__.__name__))


def main():
    short_jump = ShortJump()
    long_jump = LongJump()
    tornado_kick = TornadoKick()

    ramesh = Ramesh(short_jump, tornado_kick)
    ramesh.display()

    ramesh.punch()
    ramesh.kick()
    ramesh.jump()

    ramesh.set_jump_behavior(long_jump)
    ramesh.jump()

if __name__ == '__main__':
    main()




