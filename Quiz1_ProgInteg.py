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
  while True:
    senha = input()
    if not senha:
      break
    if validar_senha(senha):
      print("Senha valida.")
    else:
      print("Senha invalida.")

if __name__ == "__main__":
  main()