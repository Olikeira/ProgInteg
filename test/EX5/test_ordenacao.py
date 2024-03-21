import pytest
from ordenacao import ordenar_crescente, ordenar_decrescente

def test_ordenar_crescente():
    assert ordenar_crescente([3, 1, 4, 2]) == [1, 2, 3, 4]
    assert ordenar_crescente([5, 3, 9, 1]) == [1, 3, 5, 9]
    assert ordenar_crescente([10, 7, 8, 6]) == [6, 7, 8, 10]

def test_ordenar_decrescente():
    assert ordenar_decrescente([3, 1, 4, 2]) == [4, 3, 2, 1]
    assert ordenar_decrescente([5, 3, 9, 1]) == [9, 5, 3, 1]
    assert ordenar_decrescente([10, 7, 8, 6]) == [10, 8, 7, 6]