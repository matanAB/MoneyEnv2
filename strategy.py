import random


class BaseStrategy:
    def __init__(self, envelopes):
        self.envelopes = envelopes

    def play(self):
        """
        play the game: take an envelope and ask the player to take it or open another one
        when he take it, print the amount of money.
        :return none:
        """
        place = self.envelopes[0]
        for place in self.envelopes:
            if not place.used:
                stop_or_open = input("inside this envelope there are " + str(place.money) +
                                     "$.\nDo you want to open another envelope or stop? (write open/stop to continue).")
                while stop_or_open not in ("stop", "open"):
                    stop_or_open = input("type open or stop")
                if stop_or_open == "stop":
                    print(place.display())
                    return
                if stop_or_open == "open":
                    place.used = True
                    print("next envelope is opening now")

        print(place.display())

    def display(self):
        """
        display what this strategy is doing
        :return description:
        """
        return "take an envelope from the list, print the amount of money and ask if you want to take it. \n " \
               "it will continue taking envelopes until you choose to take it, or until there are no more envelopes."


class Automatic_BaseStrategy(BaseStrategy):
    def __init__(self, envelopes):
        super().__init__(envelopes)
        self.envelopes = envelopes

    def play(self):
        """
        play the game: take random envelope from the list of envelopes and print the amount of money
        :return none:
        """
        num = random.randrange(100)
        envelope = self.envelopes[num]
        while envelope.used:
            num = random.randrange(100)
            envelope = self.envelopes[num]
        envelope.used = True
        print(envelope.display())

    def display(self):
        """
        display what this strategy is doing
        :return description:
        """
        return "Automatic BaseStrategy - take random envelope from the list of envelopes \n " \
               "and print how much money was in the envelope and that's how much you've got."


class N_max_strategy(BaseStrategy):
    def __init__(self, envelopes):
        super().__init__(envelopes)
        self.envelopes = envelopes
        self.N = 3

    def play(self):
        """
        play the game: open the envelopes until we find N envelopes with max money and then stop
                       and print the amount of money
        :return none:
        """
        max_money = 0
        count = 0
        index = 0
        max_env = self.envelopes[0]
        while index < 100 and count < self.N:
            if self.envelopes[index].money > max_money and not self.envelopes[index].used:
                max_money = self.envelopes[index].money
                count += 1
                max_env = self.envelopes[index]
            self.envelopes[index].used = True
            index += 1
        if count != self.N:
            # if we didn't found N maxes- meaning the while stopped because we got to the last envelope
            # the "max_env" should be the last one
            max_env = self.envelopes[99]
        print(max_env.display())

    def display(self):
        """
        display what this strategy is doing
        :return description:
        """
        return "N max strategy - find N max envelopes, and when it found N maxes it stops \n " \
               "and print how much money was in the last envelope and that's how much you've got."


class More_then_N_percent_group_strategy(BaseStrategy):
    def __init__(self, envelopes, percent):
        super().__init__(envelopes)
        self.envelopes = envelopes
        self.percent = float(int(percent))

    def play(self):
        """
        play the game: opens x% of envelopes and chooses the envelope with the highest amount of money inside.
                       Then it compares the amount of money to the other 100% - x% of the envelopes and if a
                       higher amount is found it will replace the envelope and immediately print the amount of
                       money of the new envelope
        :return None:
        """
        opened_env = 0
        highest_amount = self.envelopes[opened_env].money
        opened_env = 1
        absolute_highest_amount = 0
        env_to_return = self.envelopes[opened_env]
        while (float(self.percent) * 100) > float(opened_env):
            if self.envelopes[opened_env].money > highest_amount:
                highest_amount = self.envelopes[opened_env].money
                env_to_return = self.envelopes[opened_env]
            self.envelopes[opened_env - 1].used = True
            opened_env = opened_env + 1
        absolute_highest_amount = highest_amount
        while opened_env < 100:
            if self.envelopes[opened_env].money > absolute_highest_amount:
                absolute_highest_amount = self.envelopes[opened_env].money
                env_to_return = self.envelopes[opened_env]
                break
            self.envelopes[opened_env].used = True
            opened_env = opened_env + 1
        if opened_env == 100:
            # if the while ended and we didn't found our max envelope the "env_to_return" should be the last one
            env_to_return = self.envelopes[99]
        print("you got: " + str(env_to_return.money) + " dollars")

    def display(self):
        """
        display what this strategy is doing
        :return description:
        """
        return ("opens x% of envelopes and chooses the envelope \n "
                "with the highest amount of money inside. then it \n "
                "compares the amount of money to the other 100% - x% \n "
                "of the envelopes and if a higher amount is found \n"
                "it will replace the envelope and immediately return the new envelope")
