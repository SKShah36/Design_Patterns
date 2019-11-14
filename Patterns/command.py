# This code is adapted from https://www.geeksforgeeks.org/command-pattern/

import abc
from abc import ABC, abstractmethod


class Command(metaclass=abc.ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class Light:
    def on(self):
        print("Light is on")

    def off(self):
        print("Light is on")


class LightOnCommand(Command):
    def __init__(self, light: Light):
        self._light = light

    def execute(self):
        self._light.on()


class LightOffCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.off()


class Stereo:
    def on(self):
        print("Stereo is on")

    def off(self):
        print("Stereo is off")

    def setCD(self):
        print("Stereo is set for CD input")

    def setDVD(self):
        print("Stereo is set for DVD input")

    def setRadio(self):
        print("Stereo is set for Radio")

    def setVolume(self, volume: int):
        print("Stereo volume set to {}".format(volume))


class StereoOffCommand(Command):
    def __init__(self, stereo: Stereo):
        self._stereo = stereo

    def execute(self):
        self._stereo.off()


class StereoOnWithCDCommand(Command):
    def __init__(self, stereo: Stereo):
        self._stereo = stereo

    def execute(self):
        self._stereo.on()
        self._stereo.setCD()
        self._stereo.setVolume(11)


class SimpleRemoteControl:
    def __init__(self):
        self._slot = None

    def setCommand(self, command: Command):
        self._slot = command

    def button_was_pressed(self):
        self._slot.execute()


def driver():
    remote = SimpleRemoteControl()
    light = Light()
    stereo = Stereo()

    remote.setCommand(LightOnCommand(light))
    remote.button_was_pressed()
    remote.setCommand(StereoOnWithCDCommand(stereo))
    remote.button_was_pressed()
    remote.setCommand(StereoOffCommand(stereo))
    remote.button_was_pressed()


if __name__ == "__main__":
    driver()
