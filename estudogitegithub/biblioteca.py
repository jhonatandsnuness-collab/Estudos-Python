import time

tarefas = []
#comentáio aleatório
while True:
    item = input("Digite uma tarefa ou 'sair': ")

    if item.lower() == "sair":
        break

    horario = time.strftime('%H:%M:%S')
    tarefas.append(F"{item} (adicionada às {horario})")

print("\nLista final de tarefas:")
for t in tarefas:
    print("-", t)
    print("-", t)