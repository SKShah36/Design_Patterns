'''
The following code is adapted from https://www.geeksforgeeks.org/proxy-design-pattern/
'''

import abc


class Internet(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def connect_to(self, server_host: str) -> None:
        pass


class RealInternet(Internet):
    def connect_to(self, server_host: str) -> None:
        print("Connecting to {}".format(server_host))


class ProxyInternet(Internet):
    _bannedSites = ["abc.com", "def.com", "ijk.com", "lnm.com"]

    def __init__(self):
        self._internet = RealInternet()

    def connect_to(self, server_host: str) -> None:
        assert server_host.lower() not in ProxyInternet._bannedSites
        self._internet.connect_to(server_host)


def driver():
    internet = ProxyInternet()
    try:
        internet.connect_to("imo.org")
        internet.connect_to("abc.com")
    except AssertionError:
        print("Access denied")


if __name__ == "__main__":
    driver()