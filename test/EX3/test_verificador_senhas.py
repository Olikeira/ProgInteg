from verificador_senhas import verificar_senha_segura

def test_verificar_senha_segura():
    # Senhas que atendem aos critérios
    assert verificar_senha_segura("Abcd@123") == True
    assert verificar_senha_segura("SenhaSegura@") == True
    
    # Senhas que não atendem aos critérios
    assert verificar_senha_segura("abc") == False
    assert verificar_senha_segura("ABC") == False
    assert verificar_senha_segura("12345678") == False
    assert verificar_senha_segura("senhafraca") == False