class No:
    def __init__(self, operacao):
        self.operacao = operacao
        self.proximo = None


def inserir(pilha, operacao):
    novo = No(operacao)
    novo.proximo = pilha
    pilha = novo
    return pilha


def remover(pilha):
    if pilha is None:
        print("Pilha vazia")
        return None

    print("Operação retirada:", pilha.operacao)

    pilha = pilha.proximo
    return pilha


def topo(pilha):
    if pilha is None:
        print("Pilha vazia")
    else:
        print("Última operação inserida:", pilha.operacao)


def listar(pilha):
    if pilha is None:
        print("Pilha vazia")
        return

    aux = pilha
    contador = 1

    while aux is not None:
        print(contador, "-", aux.operacao)
        contador += 1
        aux = aux.proximo


def menu():
    print("1 - Inserir operação na pilha")
    print("2 - Retirar última operação")
    print("3 - Mostrar última operação")
    print("4 - Mostrar todas as operações pendentes")
    print("5 - Sair")

    opcao = int(input("Digite sua opção: "))
    return opcao


def main():
    opcao = 0
    pilha = None

    while opcao != 5:
        opcao = menu()

        if opcao == 1:
            operacao = input("Digite a operação: ")
            pilha = inserir(pilha, operacao)

        elif opcao == 2:
            pilha = remover(pilha)

        elif opcao == 3:
            topo(pilha)

        elif opcao == 4:
            listar(pilha)

        elif opcao == 5:
            print("Encerrando...")

        else:
            print("Erro, tente novamente")

main()
