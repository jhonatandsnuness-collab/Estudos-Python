numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_dobrados = []

for numero in numeros:
    numeros_dobrados.append(numero * 2)

    print(numeros_dobrados)


numeros = [11, 22, 33, 44, 55, 66, 77, 88]
numeros_somados = []

def soma(numero):
    return numero + 11

numeros_somados = [numero + 11 for numero in numeros]

print(numeros_somados)

# numeros = [12, 13, 14, 15, 16, 17, 18, 19]
numeros_subtraidos = []

def subtracao(numero):
    return numero - 1

numeros_subtraidos = [numero - 1 for numero in numeros]