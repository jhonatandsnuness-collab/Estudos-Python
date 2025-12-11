numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_dobrados = []

# exp for item in list
for numero in numeros:
    numeros_dobrados.append(numero * 2)

    print(numeros_dobrados)


numeros = [11, 22, 33, 44, 55, 66, 77, 88]
numeros_somados = []

def soma(numero):
    return numero + 11

numeros_somados = [numero + 11 for numero in numeros]

print(numeros_somados)

# Uma outra forma:
numeros = [12, 13, 14, 15, 16, 17, 18, 19]

def subtracao(numero):
    return numero - 1

numeros_subtraidos = [subtracao(numero) for numero in numeros]
print(numeros_subtraidos)

# Nova lista:
nomes = ['Jhonatan', 'Douglas', 'Gilson', 'Geniva']
# Passando como condicional se a primeira letra for iniciada com G colocar em caixa alta.
nomes_maiusculos = [nome.upper() for nome in nomes if nome[0] == 'G'] 
print(nomes_maiusculos)

