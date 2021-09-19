from typing import Protocol
from dataclasses import dataclass


@dataclass
class Country(Protocol):
    name: str

    def say_hi(self):
        print(f"My name is {self.name}, from {self.__class__.__name__}")


@dataclass
class Taiwan:
    name: str

    def say_hi(self):
        print(f"My name is {self.name}, from {self.__class__.__name__}")


@dataclass
class HongKong:
    name: str

    def say_hi(self):
        print(f"My name is {self.name}, from {self.__class__.__name__}")


nation_dict = {}


def register(nation_name: str, nation_fn: Country):
    nation_dict[nation_name] = nation_fn


def create(arguments):
    args = arguments.copy()
    country = args.pop('country')
    return nation_dict[country](**args)


def test_register():
    register('Taiwan', Taiwan)
    assert 'Taiwan' in nation_dict


def test_create():
    register('Taiwan', Taiwan)
    args = dict(country="Taiwan", name='henry')
    assert Taiwan('henry') == create(args)
