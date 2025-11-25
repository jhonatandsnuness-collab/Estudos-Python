import random
import string

tamanho = int(input("Tamanho da senha: "))

caracteres = list(string.ascii_letters + string.digits)

senha = "".join(random.choice(caracteres) for _ in range(tamanho))

print("Senha gerada:", senha)