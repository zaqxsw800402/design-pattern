from __future__ import annotations
from typing import Protocol, List


class Source:
    def __init__(self):
        self.list = []  # type: List[Observer]
        self.value = 0  # type: int

    def set_value(self, value):
        self.value = value
        self._send_value()

    def get_value(self):
        return self.value

    def add_observer(self, ob: Observer):
        self.list.append(ob)
        ob.add_sources(self)

    def delete_observer(self, ob: Observer):
        self.list.remove(ob)

    def _send_value(self):
        for observer in self.list:
            observer.update()


class Observer(Protocol):
    def add_sources(self, source: Source):
        pass

    def update(self):
        pass


class FirstObserver:
    def __init__(self):
        self.value = 100

    def add_sources(self, source):
        self.source = source

    def update(self):
        self.value -= self.source.get_value()
        print(self.value)


class SecondObserver:
    def __init__(self):
        self.value = 100

    def add_sources(self, source):
        self.source = source

    def update(self):
        self.value += self.source.get_value()
        print(self.value)


def add_values(source: Source):
    while True:
        try:
            value = int(input('what value would you like to add to source: '))
            source.set_value(value)
        except ValueError:
            break


if __name__ == '__main__':
    source = Source()
    fo = FirstObserver()
    so = SecondObserver()
    source.add_observer(fo)
    source.add_observer(so)
    add_values(source)
    source.delete_observer(so)
    source.set_value(50)
    print(so.value)
