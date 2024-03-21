import re

def validar_telefone(numero):
    # Expressão regular para validar o número de telefone com DDD
    padrao = r'^\(\d{2}\)\s?9?\d{4}-\d{4}$'
    return re.match(padrao, numero) is not None
