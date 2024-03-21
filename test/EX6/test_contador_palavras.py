import pytest
from contador_palavras import contar_palavras

def test_contar_palavras():
    assert contar_palavras("Isso é um teste") == 4
    assert contar_palavras("Conte as palavras neste texto") == 5
    assert contar_palavras("Uma palavra") == 2
    assert contar_palavras("") == 0