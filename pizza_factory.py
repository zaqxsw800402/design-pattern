from abc import ABC, abstractmethod


class Source(ABC):
    @abstractmethod
    def soil(self):
        pass

    @abstractmethod
    def paper(self):
        pass


class CK(Source):
    def soil(self):
        print('Using CK soil')

    def paper(self):
        print('Using CK paper')


class JP(Source):
    def soil(self):
        print('Using JP soil')

    def paper(self):
        print('Using JP paper')


class Pizza(ABC):

    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def cut(self):
        pass


class Hawayi(Pizza):
    def __init__(self, source: Source = CK()):
        self.source = source

    def bake(self):
        self.source.soil()
        print("Hawayi bake")

    def cut(self):
        self.source.paper()
        print('Hawayi cut')


class Taiwan(Pizza):
    def __init__(self, source: Source = JP()):
        self.source = source

    def bake(self):
        self.source.soil()
        print('Taiwan bake')

    def cut(self):
        self.source.paper()
        print('Taiwan cut')


class PizzaFactory(ABC):
    def create_pizza(self, name: str) -> Pizza:
        pass


class TaiwanFactory(PizzaFactory):
    def create_pizza(self, name) -> Pizza:
        if name == 'Taiwan':
            return Taiwan()
        elif name == 'Hawayi':
            return Hawayi()


class HKFactory(PizzaFactory):
    def create_pizza(self, name) -> Pizza:
        if name == 'Taiwan':
            return Taiwan()
        elif name == 'Hawayi':
            return Hawayi()


class PizzaStore(ABC):
    @abstractmethod
    def _create_pizza(self, pizza_name: str) -> Pizza:
        pass

    @abstractmethod
    def order(self, pizza_name: str):
        pass


class TaiwanStore(PizzaStore):
    def __init__(self):
        self.factory = TaiwanFactory()

    def _create_pizza(self, pizza_name: str):
        return self.factory.create_pizza(pizza_name)

    def order(self, pizza_name: str):
        pizza = self._create_pizza(pizza_name)
        pizza.bake()
        pizza.cut()


if __name__ == '__main__':
    tw = TaiwanStore()
    tw.order('Taiwan')
    tw.order('Hawayi')
