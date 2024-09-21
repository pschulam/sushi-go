import random
from typing import List

import sushi_go.cards
from sushi_go.cards import Card
from sushi_go.scoring import score_drafted


_NEW_DECK_COUNTS = [
    (sushi_go.cards.Tempura, 14),
    (sushi_go.cards.Sashimi, 14),
    (sushi_go.cards.Dumpling, 14),
    (sushi_go.cards.Maki1, 6),
    (sushi_go.cards.Maki2, 12),
    (sushi_go.cards.Maki3, 8),
    (sushi_go.cards.SalmonNigiri, 10),
    (sushi_go.cards.SquidNigiri, 5),
    (sushi_go.cards.EggNigiri, 5),
    (sushi_go.cards.Pudding, 10),
    (sushi_go.cards.Wasabi, 6),
    (sushi_go.cards.Chopsticks, 4),
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
