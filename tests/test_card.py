import random

from game_parts import Card


def test_card_range(monkeypatch):
    monkeypatch.setattr(random, 'sample', lambda _, _2: [2, 1, 5, 3, 14, 11, 10, 8, 22, 7, 30, 44, 18, 23, 56])
    monkeypatch.setattr(random, 'randint', lambda _, _2: 3)
    card = Card()
    assert card.card_rows[0] == [1, 2, 3, '', '', '', '', 5, 14]
    assert card.card_rows[1] == [7, 8, 10, '', '', '', '', 11, 22]
    assert card.card_rows[2] == [18, 23, 30, '', '', '', '', 44, 56]


def test_number_is_crossed_in_card():
    card = Card()
    card.card_rows = [[1, 2, 3], [4, 5, 6]]
    card_rows = card.cross_number(3)
    print(card_rows)


def test_card_contains_number():
    card = Card()
    card.card_rows = [[1, 2, 3], [4, 5, 6]]
    assert card.contains(3) is True


def test_card_not_contains_number():
    card = Card()
    card.card_rows = [[1, 2, 3], [4, 5, 6]]
    assert card.contains(10) is False


def test_if_everything_crossed_in_card():
    card = Card()
    card.card_rows = [["-", "", ""], ["-", "-", ""]]
    assert card.if_everything_crossed() is True

def test_if_everything_not_crossed_in_card():
    card = Card()
    card.card_rows = [[1, "-", 3], [4, "", 6]]
    assert card.if_everything_crossed() is False
