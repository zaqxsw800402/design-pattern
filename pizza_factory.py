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


class HongKong(Pizza):
    def __init__(self, source: Source = JP()):
        self.source = source

    def bake(self):
        self.source.soil()
        print('HongKong bake')

    def cut(self):
        self.source.paper()
        print('HongKong cut')


class PizzaFactory(ABC):
    def create_pizza(self, name: str, source: Source) -> Pizza:
        pass


class TaiwanFactory(PizzaFactory):
    pizza = {'Taiwan': Taiwan, 'Hawayi': Hawayi}

    def create_pizza(self, name, source) -> Pizza:
        return self.pizza.get(name, 'Taiwan')(source)


class HKFactory(PizzaFactory):
    pizza = {'HongKong': HongKong, 'Hawayi': Hawayi}

    def create_pizza(self, pizza_name, source) -> Pizza:
        return self.pizza.get(pizza_name, 'HongKong')(source)


class PizzaStore(ABC):
    @abstractmethod
    def _create_pizza(self, pizza_name, source: Source) -> Pizza:
        pass

    @abstractmethod
    def order(self, pizza_name, source: Source):
        pass


class TaiwanStore(PizzaStore):
    def __init__(self, factory: PizzaFactory = TaiwanFactory()):
        self.factory = factory

    def change_factory(self, factory: PizzaFactory):
        self.factory = factory

    def _create_pizza(self, pizza_name: str, source: Source):
        return self.factory.create_pizza(pizza_name, source)

    def order(self, pizza_name: str, source: Source):
        pizza = self._create_pizza(pizza_name, source)
        pizza.bake()
        pizza.cut()


if __name__ == '__main__':
    tw = TaiwanStore()
    jp_source = JP()
    ck_source = CK()
    tw.order('Taiwan', jp_source)
    tw.order('Hawayi', ck_source)
    print('------------')
    tw.change_factory(HKFactory())
    tw.order('HongKong', jp_source)
    tw.order('Hawayi', ck_source)
