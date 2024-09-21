from typing import List

import sushi_go.cards
from sushi_go.cards import Card


def score_drafted(cards: List[Card]) -> int:
    points = 0
    points += _score_drafted_tempura(cards)
    points += _score_drafted_sashimi(cards)
    points += _score_drafted_dumplings(cards)
    points += _score_drafted_nigiri(cards)
    return points


def _score_drafted_tempura(cards: List[Card]) -> int:
    n_tempura = sum(isinstance(card, sushi_go.cards.Tempura) for card in cards)
    return 5 * (n_tempura // 2)


def _score_drafted_sashimi(cards: List[Card]) -> int:
    n_sashimi = sum(isinstance(card, sushi_go.cards.Sashimi) for card in cards)
    return 10 * (n_sashimi // 3)


def _score_drafted_dumplings(cards: List[Card]) -> int:
    dumpling_points = {0: 0, 1: 1, 2: 3, 3: 6, 4: 10, 5: 15}
    n_dumplings = sum(isinstance(card, sushi_go.cards.Dumpling) for card in cards)
    if n_dumplings in dumpling_points:
        return dumpling_points[n_dumplings]
    else:
        assert n_dumplings > max(dumpling_points)
        return dumpling_points[max(dumpling_points)]


def _score_drafted_nigiri(cards: List[Card]) -> int:
    def get_multiplier():
        if n_wasabi > 0:
            n_wasabi -= 1
            return 3
        else:
            return 1
    points = 0
    n_wasabi = 0
    for card in cards:
        if isinstance(card, sushi_go.cards.Wasabi):
            n_wasabi += 1
        if isinstance(card, sushi_go.cards.EggNigiri):
            points += get_multiplier() * 1
        if isinstance(card, sushi_go.cards.SalmonNigiri):
            points += get_multiplier() * 2
        if isinstance(card, sushi_go.cards.SquidNigiri):
            points += get_multiplier() * 3
