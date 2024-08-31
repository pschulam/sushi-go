import random
from typing import List

from . import cards
from .cards import Card


_NEW_DECK_COUNTS = [
    (cards.Tempura, 14),
    (cards.Sashimi, 14),
    (cards.Dumpling, 14),
    (cards.Maki1, 6),
    (cards.Maki2, 12),
    (cards.Maki3, 8),
    (cards.SalmonNigiri, 10),
    (cards.SquidNigiri, 5),
    (cards.EggNigiri, 5),
    (cards.Pudding, 10),
    (cards.Wasabi, 6),
    (cards.Chopsticks, 4),
]


def new_deck() -> List[Card]:
    return [
        card_class()
        for card_class, count in _NEW_DECK_COUNTS
        for _ in range(count)
    ]


def deal_hands(num_players: int, deck: List[Card], seed=0) -> List[List[Card]]:
    assert 2 <= num_players <= 5
    cards_per_player = {2: 10, 3: 9, 4: 8, 5: 7}[num_players]
    rng = random.Random(seed)
    rng.shuffle(deck)
    return [
        [deck.pop() for _ in range(cards_per_player)]
        for _ in range(num_players)
    ]


def score_drafted(cards: List[Card]) -> int:
    pass
