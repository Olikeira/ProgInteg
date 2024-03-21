from diferenca_datas import diferenca_entre_datas

def test_diferenca_entre_datas():
    # Diferença de 1 dia
    assert diferenca_entre_datas('2024-03-20 12:00:00', '2024-03-21 12:00:00', 'dias') == 1
    
    # Diferença de 1 mês
    assert diferenca_entre_datas('2024-03-20 12:00:00', '2024-04-20 12:00:00', 'meses') == 1
    
    # Diferença de 1 ano
    assert diferenca_entre_datas('2024-03-20 12:00:00', '2025-03-20 12:00:00', 'anos') == 1
    
    # Diferença de 24 horas
    assert diferenca_entre_datas('2024-03-20 12:00:00', '2024-03-21 12:00:00', 'horas') == 24
    
    # Diferença de 60 minutos
    assert diferenca_entre_datas('2024-03-20 12:00:00', '2024-03-20 13:00:00', 'minutos') == 60
