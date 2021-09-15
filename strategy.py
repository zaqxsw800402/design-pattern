from typing import Protocol


class Toy(Protocol):
    def run(self):
        pass

    def jump(self):
        pass


class Tank(Toy):
    def run(self):
        print('Tank is running')

    def jump(self):
        print('Tank has jump')


class Helicopter(Toy):
    def run(self):
        print('Helicopter is flying')

    def jump(self):
        print('Helicopter can not jump')


class Player:
    def __init__(self, toy: Toy):
        self.toy = toy

    def change_toy(self, toy: Toy):
        self.toy = toy

    def toy_jump(self):
        self.toy.jump()

    def toy_run(self):
        self.toy.run()


if __name__ == '__main__':
    player = Player(Tank())
    player.toy_jump()
    player.toy_run()
    player.change_toy(Helicopter())
    player.toy_jump()
    player.toy_run()
