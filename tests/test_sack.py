import random

from game_parts import Sack


def test_balls_list_contains_90_balls():
    sack = Sack()
    expected = list(range(1, 91))
    assert sack.balls == expected


def test_current_ball_id(monkeypatch):
    sack = Sack()
    monkeypatch.setattr(random, 'choice', lambda _: 1)
    assert sack.get_current_number() == 2


def test_current_ball_deleted_from_sack(monkeypatch):
    sack = Sack()
    monkeypatch.setattr(random, 'choice', lambda _: 1)
    sack.get_current_number()
    assert 2 not in sack.balls
    assert len(sack.balls) == 89



