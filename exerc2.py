#1 Crie uma função que conte o número de vogais em uma string. 
def contarVogais(string):
    vogais = 'aeiouAEIOU'
    contador = 0 
    for char in string:
        if char in vogais:
            contador += 1
    return contador

inpQualquer = input ('Digite qualquer coisa: ')
print("sua frase tem: ", contarVogais(inpQualquer), "vogais")

#2 Escreva um programa que substitua todas as ocorrências de uma letra em uma
#string por outra letra. 
def substituirLetra (string, Letra_antiga, Letra_nova):
    nova_string = string.replace (letra_antiga, Letra_nova)
    return nova_string

string_original = input("Digite sua frase: ")
letra_antiga = input ("Digite a letra que deve ser substituída: ")
letra_nova = input ("Digite a nova letra que deve substituí-la: ")

nova_string = substituirLetra (string_original, letra_antiga, letra_nova)
print("sua str com a letra substituída fica: ", nova_string)

#3 Crie uma função que retorne o número de palavras em uma string
def contar_palavras(string):
    palavras = string.split()
    return len(palavras)

frase = input ("Digite sua frase: ")
num_frase = contar_palavras(frase)
print("Sua frase tem: ", num_frase, "palavras")

#4 Crie uma função que conte o número de ocorrências de uma determinada palavra
#em uma frase.
def ocor_palavra(frase, palavra):
    numeroocorrencias = frase.lower().count(palavra.lower())
    return numeroocorrencias

frase = input("Digite um texto e veremos quantas vezes alguma palavra se repete: ")
palavra_procurada = input("Digite a palavra que você quer saber quantas vezes se repete: ")
numeroocorrencias = ocor_palavra (frase, palavra_procurada)
print(f"A palavra procurada aparece '{numeroocorrencias}' vezes")

#5 Crie uma função que encontre os k maiores elementos em uma lista, mantendo a
#ordem original
def encontrar_k_maiores(lista, k):

  if k <= 0:
    return []

  if k >= len(lista):
    return lista

  heap_max = lista[:k]
  heapq.heapify(heap_max)

  for elemento in lista[k:]:
    if elemento > heap_max[0]:
      heapq.heappop(heap_max)
      heapq.heappush(heap_max, elemento)


  return heapq.nlargest(k, heap_max)


lista = input("Digite os elementos da lista (separados por vírgula): ").split(",")
lista = [int(x) for x in lista]

k = int(input("Digite o valor de k: "))

maiores = encontrar_k_maiores(lista, k)

print(f"Lista original: {lista}")
print(f"K maiores elementos: {maiores}")

#6. Escreva um programa que implemente a soma de matrizes usando listas
#aninhadas.
def soma_matrizes(matrizA, matrizB):
    num_linhas_A, num_colunas_A = len(matrizA), len(matrizA[0])
    num_linhas_B, num_colunas_B = len(matrizB), len(matrizB[0])
    
    if num_linhas_A != num_linhas_B or num_colunas_A != num_colunas_B:
        return "As matrizes devem ter as mesmas dimensões para serem somadas!"
    
    matriz_soma = [[0 for _ in range(num_colunas_A)] for _ in range(num_linhas_A)]
    
    for i in range(num_linhas_A):
        for j in range(num_colunas_A):
            matriz_soma[i][j] = matrizA[i][j] + matrizB[i][j]
    
    return matriz_soma

matrizA = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrizB = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

resultado = soma_matrizes(matrizA, matrizB)

if type(resultado) is str:
    print(resultado)
else:
    for linha in resultado:
        print(linha)

#7. Crie uma função que encontre a interseção de duas listas sem usar conjuntos.
def intersecao_listas(lista1, lista2):
    intersecao = [item for item in lista1 if item in lista2]
    resultado = []
    for item in intersecao:
        if item not in resultado:
            resultado.append(item)
    return resultado

lista1 = [1, 2, 3, 4, 5, 5, 6]
lista2 = [4, 5, 6, 7, 8]
print(intersecao_listas(lista1, lista2))

#9. Escreva um programa que encontre o par de elementos em uma lista cuja soma
#seja igual a um determinado valor.
def encontrar_par_soma(lista, soma_alvo):
    visto = set()
    for numero in lista:
        complemento = soma_alvo - numero
        if complemento in visto:
            return (complemento, numero)
        visto.add(numero)
    return None 

lista = [2, 4, 5, 1, 3, 9, 8, 6]
soma_alvo = 10

resultado = encontrar_par_soma(lista, soma_alvo)

if resultado:
    print(f"Par encontrado: {resultado}")
else:
    print("Nenhum par encontrado.")

#10.Criar um algoritmo para calcular a frequência que uma palavra aparece em um
texto
def calcular_frequencia_palavras(texto):
    texto = texto.replace('.', '').replace(',', '').replace(';', '').replace('?', '').replace('!', '').lower()
    palavras = texto.split() 
    
    frequencias = {}  
    
    for palavra in palavras:
        if palavra in frequencias:
            frequencias[palavra] += 1 
        else:
            frequencias[palavra] = 1 
    
    return frequencias

texto = "O rato roeu a roupa do rei de Roma. A rainha, raivosa, rasgou o resto."
frequencia = calcular_frequencia_palavras(texto)

for palavra, freq in frequencia.items():
    print(f"'{palavra}': {freq}")

#11. Escreva um programa que identifique todos os números primos em uma lista de
#números inteiros.
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def identificar_primos(lista):
    primos = [n for n in lista if eh_primo(n)]
    return primos

lista_numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 29, 37, 41, 42]
numeros_primos = identificar_primos(lista_numeros)

print("Números primos na lista:", numeros_primos)

