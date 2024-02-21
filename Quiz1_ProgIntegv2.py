def validar_senha(senha):
  if len(senha) < 6 or len(senha) > 32:
    return False
  for char in senha:
    if not char.isalnum():
      return False
  tem_maiuscula = False
  tem_minuscula = False
  for char in senha:
    if char.isupper():
      tem_maiuscula = True
    elif char.islower():
      tem_minuscula = True
  if not tem_maiuscula or not tem_minuscula:
    return False
  return True

def main():
  print("Olá! Vamos verificar a força da sua senha.")
  print("---------------------------------------")
  while True:
    senha = input("Digite sua senha: ")
    if not senha:
      break
    if validar_senha(senha):
      print("Senha válida!")
      print("---------------------------------------")
    else:
      print("Senha inválida!")
      print("Sua senha deve ter entre 6 e 32 caracteres,")
      print("conter letras maiúsculas e minúsculas e")
      print("não ter caracteres especiais.")
      print("---------------------------------------")

if __name__ == "__main__":
  main()