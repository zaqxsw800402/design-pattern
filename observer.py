from __future__ import annotations
from typing import Protocol, List


class Source:
    def __init__(self):
        self.list = []  # type: List[Observer]
        self.value = 0  # type: int

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def add_observer(self, ob: Observer):
        self.list.append(ob)
        ob.add_sources(self)

    def send_value(self):
        for observer in self.list:
            observer.update()


class Observer(Protocol):

    def add_sources(self, source):
        pass

    def update(self):
        pass


class FirstObserver(Observer):
    def __init__(self):
        self.value = 0

    def add_sources(self, source):
        self.source = source

    def update(self):
        self.value = self.source.get_value()


class SecondObserver(Observer):
    def __init__(self):
        self.value = 0

    def add_sources(self, source):
        self.source = source

    def update(self):
        self.value = self.source.get_value()


if __name__ == '__main__':
    source = Source()
    fo = FirstObserver()
    so = SecondObserver()
    source.add_observer(fo)
    source.add_observer(so)
    print(fo.value)
    source.set_value(5)
    source.send_value()
    print(fo.value)
    source.set_value(10)
    source.send_value()
    print(so.value)
    print(so.source)
