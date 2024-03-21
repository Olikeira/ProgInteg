import pytest
from sistema_reservas import Voo, SistemaReservas

def test_adicionar_voo():
    sistema = SistemaReservas()
    voo = Voo("AB123", "São Paulo", "Rio de Janeiro", "2024-03-25", "08:00")
    sistema.adicionar_voo(voo)
    assert len(sistema.voos) == 1

def test_realizar_reserva():
    sistema = SistemaReservas()
    voo = Voo("AB123", "São Paulo", "Rio de Janeiro", "2024-03-25", "08:00")
    sistema.adicionar_voo(voo)
    reserva = sistema.realizar_reserva("AB123", "João")
    assert reserva.voo == voo
    assert reserva.passageiro == "João"

def test_cancelar_reserva():
    sistema = SistemaReservas()
    voo = Voo("AB123", "São Paulo", "Rio de Janeiro", "2024-03-25", "08:00")
    sistema.adicionar_voo(voo)
    reserva = sistema.realizar_reserva("AB123", "João")
    assert sistema.cancelar_reserva(reserva) == True
    assert len(sistema.reservas) == 0

def test_visualizar_reservas():
    sistema = SistemaReservas()
    voo1 = Voo("AB123", "São Paulo", "Rio de Janeiro", "2024-03-25", "08:00")
    voo2 = Voo("CD456", "Rio de Janeiro", "São Paulo", "2024-03-25", "10:00")
    sistema.adicionar_voo(voo1)
    sistema.adicionar_voo(voo2)
    reserva1 = sistema.realizar_reserva("AB123", "João")
    reserva2 = sistema.realizar_reserva("CD456", "Maria")
    reservas = sistema.visualizar_reservas()
    assert len(reservas) == 2
    assert reserva1 in reservas
    assert reserva2 in reservas