from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def run(self):
        pass

    def close(self):
        pass


class Light(Product):
    def run(self):
        print('Light on')

    def close(self):
        print('Light off')


class Computer(Product):
    def run(self):
        print('Computer on')

    def close(self):
        print('Computer off')


class Controller:
    def __init__(self):
        self.slot = []

    def add_slot(self, product: Product):
        self.slot.append(product)

    def command_run(self, position: int):
        self.slot[position].run()

    def command_close(self, position: int):
        self.slot[position].close()


if __name__ == '__main__':
    controller = Controller()
    controller.add_slot(Light())
    controller.add_slot(Computer())
    controller.command_run(1)
    controller.command_close(1)
    controller.command_run(0)
