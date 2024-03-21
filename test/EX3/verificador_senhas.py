import re

def verificar_senha_segura(senha):
    # Verifica o comprimento mínimo
    if len(senha) < 8:
        return False
    
    # Verifica se há pelo menos um caractere maiúsculo
    if not re.search("[A-Z]", senha):
        return False
    
    # Verifica se há pelo menos um caractere minúsculo
    if not re.search("[a-z]", senha):
        return False
    
    # Verifica se há pelo menos um caractere especial
    if not re.search("[!@#$%^&*()\-_=+{};:,<.>]", senha):
        return False
    
    return True