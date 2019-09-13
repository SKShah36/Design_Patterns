
class Singleton:
    __instance = None

    class __Implementation:
        def test_instance(self):
            return id(self)

    def __init__(self):
        if Singleton.__instance is None:
            Singleton.__instance = Singleton.__Implementation()

    def __getattr__(self, item):
        return getattr(self.__instance, item)


s1 = Singleton()
#print(id(s1), s1.test_instance())
s1.__getattr__("test_instance")
s2 = Singleton()
print(s2.test_instance())



