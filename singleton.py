def passfunc(*args, **kwargs):
    pass


class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = object.__new__(cls)
        else:
            cls.__init__ = passfunc
        return cls.instance


class Counter:
    def __init__(self, initial_count=0, step=1):
        self.count = initial_count
        self.step = step

    def increment(self):
        self.count += self.step


class GlobalCounter(Singleton, Counter):
    pass


asd = GlobalCounter(10, 20)
ssd = GlobalCounter(20, 40)
print(asd.step, asd.count)
print(ssd.step, ssd.count)
print(id(asd) == id(ssd))
