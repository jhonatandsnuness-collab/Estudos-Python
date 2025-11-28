numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []
for numero in numeros:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)

numeros = [1, 2, 3, 4, 5]

numeros_dobrados = [numero * 2 for numero in numeros]
print(numeros_dobrados)

nomes = ['Jhonatan', 'Stefanny', 'Geniva', 'Gilson', 'Davi', 'Emylli']

nomes_maiusculos = [nome.upper() for nome in nomes]
print(nomes_maiusculos)

nomes = ['Jhonatan', 'Stefanny', 'Geniva', 'Gilson', 'Davi', 'Emylli']

nomes_maiusculos = [nome.upper() for nome in nomes if nome[0] == 'S']
print(nomes_maiusculos)