import pytest
from validador_telefone import validar_telefone

def test_validar_telefone():
    # Números válidos
    assert validar_telefone("(21) 98765-4321") == True
    assert validar_telefone("(11) 91234-5678") == True
    assert validar_telefone("(31) 99876-5432") == True
    
    # Números inválidos
    assert validar_telefone("2198765-4321") == False  # Sem DDD
    assert validar_telefone("(21) 987654321") == False  # Sem hífen
    assert validar_telefone("(21) 98765-432") == False  # Número incompleto
    assert validar_telefone("(21) 98765-43210") == False  # Número com mais de 8 dígitos
    assert validar_telefone("(21) 87654-3210") == False  # Número com DDD inválido
    assert validar_telefone("(aa) 98765-4321") == False  # Número com DDD inexistente
