import sushi_go
import sushi_go.cards


expected_card_counts = [
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


def test_new_deck_total_cards():
    deck = sushi_go.new_deck()
    assert len(deck) == 108


def test_new_deck_card_counts():
    deck = sushi_go.new_deck()
    for card_class, count in expected_card_counts:
        assert sum(isinstance(card, card_class) for card in deck) == count


def test_deal_hands_counts():
    game_types = [
        {'num_players': 2, 'cards_per_player': 10, 'cards_left': 88},
        {'num_players': 3, 'cards_per_player': 9,  'cards_left': 81},
        {'num_players': 4, 'cards_per_player': 8,  'cards_left': 76},
        {'num_players': 5, 'cards_per_player': 7,  'cards_left': 73},
    ]
    for game_type in game_types:
        deck = sushi_go.new_deck()
        hands = sushi_go.deal_hands(game_type['num_players'], deck)
        assert len(hands) == game_type['num_players']
        assert all(len(hand) == game_type['cards_per_player'] for hand in hands)
        assert len(deck) == game_type['cards_left']


def test_score_drafted_tempura():
    examples = [
        ([sushi_go.cards.Tempura() for _ in range(1)], 0),
        ([sushi_go.cards.Tempura() for _ in range(2)], 5),
        ([sushi_go.cards.Tempura() for _ in range(3)], 5),
        ([sushi_go.cards.Tempura() for _ in range(4)], 10),
        ([sushi_go.cards.SalmonNigiri()], 0),
    ]
    for cards, points in examples:
        assert sushi_go.score_drafted(cards) == points


def test_score_drafted_sashimi():
    examples = [
        ([sushi_go.cards.Sashimi() for _ in range(1)], 0),
        ([sushi_go.cards.Sashimi() for _ in range(2)], 0),
        ([sushi_go.cards.Sashimi() for _ in range(3)], 10),
        ([sushi_go.cards.Sashimi() for _ in range(4)], 10),
        ([sushi_go.cards.Sashimi() for _ in range(5)], 10),
        ([sushi_go.cards.Sashimi() for _ in range(6)], 20),
        ([sushi_go.cards.SalmonNigiri()], 0),
    ]
    for cards, points in examples:
        assert sushi_go.score_drafted(cards) == points


def test_score_drafted_dumplings():
    examples = [
        ([sushi_go.cards.Dumpling() for _ in range(1)], 1),
        ([sushi_go.cards.Dumpling() for _ in range(2)], 3),
        ([sushi_go.cards.Dumpling() for _ in range(3)], 6),
        ([sushi_go.cards.Dumpling() for _ in range(4)], 10),
        ([sushi_go.cards.Dumpling() for _ in range(5)], 15),
        ([sushi_go.cards.Dumpling() for _ in range(6)], 15),
        ([sushi_go.cards.SalmonNigiri()], 0),
    ]
    for cards, points in examples:
        assert sushi_go.score_drafted(cards) == points
