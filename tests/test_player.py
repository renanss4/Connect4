import pytest
from unittest.mock import patch
from classes.Player import Player

@patch('builtins.input', lambda _: '4')
def test_make_move():
    # Cria uma instância do jogador com um símbolo fictício (por exemplo, 'X')
    player = Player("Player1", "X")

    # Chama o método make_move com um argumento fictício (None neste caso)
    column = player.make_move(None)

    # Verifica se o resultado é o esperado
    assert column == 3
