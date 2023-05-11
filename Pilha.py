class Pilha:
    def __init__(pilha):
        pilha.itens = []

    def empilhar(pilha, item):
        pilha.itens.append(item)

    def desempilhar(pilha):
        if not pilha.vazia():
            return pilha.itens.pop()

    def vazia(pilha):
        return len(pilha.itens) == 0

    def topo(pilha):
        if not pilha.vazia():
            return pilha.itens[-1]

    def imprimir(pilha):
        print(list(pilha.itens))

    def imprimirRev(pilha):
        print(list(reversed(pilha.itens)))

def main():
    pilha = Pilha()

    while True:
        print("\n\n1. Inserir elemento")
        print("2. Remover elemento")
        print("3. Verificar se a pilha está vazia")
        print("4. Imprimir a pilha")
        print("5. Impressão inversa")
        print("6. Mostrar elemento do topo")
        print("7. Sair")

        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            item = input("Digite o elemento: ")
            pilha.empilhar(item)
        elif escolha == 2:
            pilha.desempilhar()
        elif escolha == 3:
            print("A pilha está:", pilha.vazia() and "vazia" or "não vazia")
        elif escolha == 4:
            pilha.imprimir()
        elif escolha == 5:
            pilha.imprimirRev()
        elif escolha == 6:
            print("Elemento do topo:", pilha.topo())
        elif escolha == 7:
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
