from collections import deque #usado para remover elementos das duas extremidades

class Fila:
    def __init__(fila):
        fila.queue = deque()

    def insere(fila, item):
        fila.queue.append(item)

    def remove(fila):
        if len(fila.queue) < 1:
            return None
        return fila.queue.popleft()

    def vazia(fila):
        return len(fila.queue) == 0

    def primeiroElemento(fila):
        return fila.queue[0] if not fila.vazia() else None

    def imprime(fila):
        for item in fila.queue:
            print(item, end=" ")
        print()

fila = Fila()

while True:
    print("\n1. Inserir um elemento")
    print("2. Remover o primeiro elemento")
    print("3. Verificar se a fila está vazia")
    print("4. Ver o primeiro elemento da fila")
    print("5. Imprimir a fila")
    print("\n6. Sair\n")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        elemento = input("Digite o elemento que deseja inserir: ")
        fila.insere(elemento)
        print(f"O elemento {elemento} foi inserido na fila.")
    elif escolha == "2":
        elemento = fila.remove()
        if elemento is None:
            print("A fila está vazia.")
        else:
            print(f"O elemento {elemento} foi removido da fila.")
    elif escolha == "3":
        if fila.vazia():
            print("A fila está vazia.")
        else:
            print("A fila não está vazia.")
    elif escolha == "4":
        elemento = fila.primeiroElemento()
        if elemento is None:
            print("A fila está vazia.")
        else:
            print(f"O primeiro elemento da fila é {elemento}.")
    elif escolha == "5":
        fila.imprime()
    elif escolha == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
