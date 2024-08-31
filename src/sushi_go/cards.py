from abc import ABC


class Card(ABC):
    pass


class Tempura(Card):
    def __str__(self):
        return 'Tempura()'


class Sashimi(Card):
    def __str__(self):
        return 'Sashimi()'


class Dumpling(Card):
    def __str__(self):
        return 'Dumpling()'


class Maki1(Card):
    def __str__(self):
        return 'Maki1()'


class Maki2(Card):
    def __str__(self):
        return 'Maki2()'


class Maki3(Card):
    def __str__(self):
        return 'Maki3()'


class SalmonNigiri(Card):
    def __str__(self):
        return 'SalmonNigiri()'


class SquidNigiri(Card):
    def __str__(self):
        return 'SquidNigiri()'


class EggNigiri(Card):
    def __str__(self):
        return 'EggNigiri()'


class Pudding(Card):
    def __str__(self):
        return 'Pudding()'


class Wasabi(Card):
    def __str__(self):
        return 'Wasabi()'


class Chopsticks(Card):
    def __str__(self):
        return 'Chopsticks()'
