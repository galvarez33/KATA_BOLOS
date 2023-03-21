import pytest


# test_bowling_game.py
def test_create_game():
    from kata import partida
    partida = partida()
    assert isinstance(partida, partida)

