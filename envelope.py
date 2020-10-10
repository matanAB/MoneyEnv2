import random


class Envelope:
    def __init__(self):
        self.money = int(random.randint(0, 10000000000))
        self.used = False

    def display(self):
        return "you got: " + str(self.money) + " dollars"
