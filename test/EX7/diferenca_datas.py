from datetime import datetime

def diferenca_entre_datas(data1, data2, unidade):
    # Converter as datas de string para objetos datetime
    data1 = datetime.strptime(data1, "%Y-%m-%d %H:%M:%S")
    data2 = datetime.strptime(data2, "%Y-%m-%d %H:%M:%S")
    
    # Calcular a diferença entre as datas
    diferenca = data2 - data1
    
    # Retornar a diferença de acordo com a unidade especificada
    if unidade == 'dias':
        return diferenca.days
    elif unidade == 'meses':
        return diferenca.days // 30
    elif unidade == 'anos':
        return diferenca.days // 365
    elif unidade == 'horas':
        return diferenca.total_seconds() // 3600
    elif unidade == 'minutos':
        return diferenca.total_seconds() // 60
    else:
        raise ValueError("Unidade de tempo inválida")