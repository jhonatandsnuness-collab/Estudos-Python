# Mostrando as linhas no terminal passando posições.
linhas = [
    "Primeria linha",
    "Segunda linha",
    "Terceira linha", 
    "Quarta linha" 
]

print(linhas[0])
print(linhas[1])
print(linhas[2])
print(linhas[3])

# Pelo usuário:
linhas = [
    "Primeria linha",
    "Segunda linha",
    "Terceira linha", 
    "Quarta linha" 
]
pos = int(input("Digite a posição da linha que deseja ver: "))
print(linhas[pos])

# Evitando um erro sem índice
linhas = [
    "Primeria linha",
    "Segunda linha",
    "Terceira linha", 
    "Quarta linha" 
]

try: 
    pos = int(input("Digite a posição da linhas: "))
    print(linhas[pos])
except IndexError: # 
    print("Erro: Essa posição não existe!")
except ValueError: # 
    print("Erro: Digite apenas um número!")


# Transformando em comando via terminal
# import sys

# linhas = [
#     "Primeria linha",
#     "Segunda linha",
#     "Terceira linha", 
#     "Quarta linha" 
# ]

# # Pega o argumento e passa no terminal
# pos = int(sys.argv[1])
# print(linhas[pos])

# Letra por letra:
texto = "Python"

print(texto[0]) # P
print(texto[1]) # y
print(texto[2]) # t
print(texto[3]) # h
print(texto[4]) # o
print(texto[5]) # n

# Acessando pela posição indicada
texto = "Programação"

pos = int(input("Digite a posição da letra: "))
print(texto[pos])

# Evintando erros:
texto = "Python"

try:
    pos = int(input("Digite a posição da letra: "))
    print(texto[pos])
except IndexError:
    print("Erro: Posição não existe na palavra!")
except ValueError:
    print("Erro: Digite apenas um número!")

# Acessando a ultima letra:
texto = "Java"
 
print(texto[-1]) # a
print(texto[-2]) # v
print(texto[-3]) # a

# Mostrando todas as letras e suas posições 
texto = "JavaScript"

for i, letra in enumerate(texto):
    print(f"Posição {i}: {letra}")

# Acessando partes do texto
texto = "Programação"

print(texto[0:4]) # Prog
print(texto[4:10]) # ramaç
print(texto[5:]) # amação
print(texto[:7]) # Program