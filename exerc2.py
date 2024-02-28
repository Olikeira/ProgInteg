#Crie uma função que conte o número de vogais em uma string. 
def contarVogais(string):
    vogais = 'aeiouAEIOU'
    contador = 0 
    for char in string:
        if char in vogais:
            contador += 1
    return contador

inpQualquer = input ('Digite qualquer coisa: ')
print("sua frase tem: ", contarVogais(inpQualquer), "vogais")

#1 Escreva um programa que substitua todas as ocorrências de uma letra em uma
#string por outra letra. 
def substituirLetra (string, Letra_antiga, Letra_nova):
    nova_string = string.replace (letra_antiga, Letra_nova)
    return nova_string

string_original = input("Digite sua frase: ")
letra_antiga = input ("Digite a letra que deve ser substituída: ")
letra_nova = input ("Digite a nova letra que deve substituí-la: ")

nova_string = substituirLetra (string_original, letra_antiga, letra_nova)
print("sua str com a letra substituída fica: ", nova_string)

#2 Crie uma função que retorne o número de palavras em uma string
def contar_palavras(string):
    palavras = string.split()
    return len(palavras)

frase = input ("Digite sua frase: ")
num_frase = contar_palavras(frase)
print("Sua frase tem: ", num_frase, "palavras")

#3 Crie uma função que conte o número de ocorrências de uma determinada palavra
#em uma frase.
def ocor_palavra(frase, palavra):
    numeroocorrencias = frase.lower().count(palavra.lower())
    return numeroocorrencias

frase = input("Digite um texto e veremos quantas vezes alguma palavra se repete: ")
palavra_procurada = input("Digite a palavra que você quer saber quantas vezes se repete: ")
numeroocorrencias = ocor_palavra (frase, palavra_procurada)
print(f"A palavra procurada aparece '{numeroocorrencias}' vezes")

#4 Crie uma função que encontre os k maiores elementos em uma lista, mantendo a
#ordem original
