class Movie:
    def turn_on(self):
        print('Turn On Movie player')

    def run(self):
        print('Movie is playing')

    def stop(self):
        print('Stop the Movie')

    def turn_off(self):
        print('Turn Off Movie player')


class Speaker:
    def turn_on(self):
        print('Turn On Speaker player')

    def turn_off(self):
        print('Turn Off Speaker player')


class Controller:
    def __init__(self):
        self.movie = Movie()
        self.speaker = Speaker()

    def run(self):
        self.movie.turn_on()
        self.movie.run()
        self.speaker.turn_on()

    def stop(self):
        self.movie.stop()
        self.movie.turn_off()
        self.speaker.turn_off()


if __name__ == '__main__':
    controller = Controller()
    controller.run()
    controller.stop()