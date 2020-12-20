import pytest

from game_parts import HumanPlayer, Card, AIPlayer


def test_player_enters_y_cross_number_returns_true(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "y")
    player = HumanPlayer(player_card=Card(), player_id=1)
    assert player.should_cross(12) is True


def test_player_enters_n_cross_number_returns_false(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "n")
    player = HumanPlayer(player_card=Card(), player_id=1)
    assert player.should_cross(12) is False


def test_if_card_contains_number_return_true(monkeypatch):
    player_card = Card()
    monkeypatch.setattr(player_card, "contains", lambda _: True)
    player = AIPlayer(player_card=player_card, player_id=1)
    assert player.should_cross(12) is True


def test_if_card_not_contains_number_return_false(monkeypatch):
    player_card = Card()
    monkeypatch.setattr(player_card, "contains", lambda _: False)
    player = AIPlayer(player_card=player_card, player_id=1)
    assert player.should_cross(12) is False
