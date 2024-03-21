from validador_emails import validar_email

def test_validar_email():
    # E-mails válidos
    assert validar_email("usuario@example.com")
    assert validar_email("joao123@gmail.com")
    
    # E-mails inválidos
    assert not validar_email("usuario@example")  # Domínio incompleto
    assert not validar_email("usuario@example.")  # Domínio vazio
    assert not validar_email("usuario.example.com")  # Sem @
    assert not validar_email("@example.com")  # Sem nome de usuário
