texto1 = 'Olá'
texto2 = 'Mundo'
texto3 = """texto
com várias
linhas"""

print(texto1)
print(texto2)
print(texto3)

nome = 'Jhonatan Douglas'
sobrenome = 'Sousa Nunes'
mensagem = nome + " " + sobrenome
print(mensagem)

risada = "ha" * 3
print(risada)

palavra = "Python"
#print(palavra[0]) # Primeiro caractere
print("") # Último caractere

frase = "Aprender Python é divertido"
print(frase[0:8]) # Caractere de 0 ao 7
print(frase[9:]) # ... do 9 até o final
print(frase[:8]) # do início até o 7
print(frase[-9:]) # últimos 9 caracteres

texto = "Python é muito maneiro"
print(texto.upper)
print(texto.lower)
print(texto.strip)
print(texto.replace("Incrível", "poderoso"))
print(texto.split)