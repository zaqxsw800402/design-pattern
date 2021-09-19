from dataclasses import dataclass
import factory


@dataclass
class Korean:
    name: str

    def say_hi(self):
        print(f"My name is {self.name}, from {self.__class__.__name__}")


def register():
    factory.register('Korean', Korean)
