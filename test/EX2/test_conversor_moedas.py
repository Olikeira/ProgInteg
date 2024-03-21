import pytest
from EX2.conversor_moedas import dolar_para_euro, real_para_dolar

def test_dolar_para_euro():
    assert dolar_para_euro(100) == 85
    assert dolar_para_euro(200) == 170
    assert dolar_para_euro(0) == 0

def test_real_para_dolar():
    assert real_para_dolar(100) == 19
    assert real_para_dolar(200) == 38
    assert real_para_dolar(0) == 0