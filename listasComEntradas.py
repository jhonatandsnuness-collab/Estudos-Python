listNumeros = [10, 20, 30, 40] # Aqui cria a lista e passa como parametro
new = int(input("Digite um número para inserir: ")) # Declara a variavel e recebe o valor inserido pelo terminal
pos = int(input("Digite a posição: ")) 

listNumeros.insert(pos, new) # Insere o valor na posição atribuida
listNumeros.append(50) # Insere o valor na ultima posição da lista
listNumeros.pop() # Remove por índice e retorna o valor removido
del listNumeros[1] # Remove por índice
listNumeros.remove(10) # Remove pelo valor
print("Lista atualizada:", listNumeros)