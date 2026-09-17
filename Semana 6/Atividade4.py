class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


def inserir(fila, dado):
    novo = No(dado)

    if fila == None:
        fila = novo
        return fila

    aux = fila

    while aux.proximo != None:
        aux = aux.proximo

    aux.proximo = novo

    return fila


def remover(fila):
    if fila == None:
        print("Fila vazia")
        return None

    return fila.proximo


def listar(fila):
    if fila == None:
        print("Fila vazia")
        return

    aux = fila
    contador = 1

    while aux != None:
        print(contador, "-", aux.dado)
        aux = aux.proximo
        contador = contador + 1


def rodada(fila):
    if fila == None:
        print("Fila vazia")
        return fila

    jogador = fila.dado

    fila = remover(fila)

    fila = inserir(fila, jogador)

    print("Jogador que participou:", jogador)
    return fila


def menu():
    print()
    print("1 - Adicionar jogador")
    print("2 - Simular 1 rodada")
    print("3 - Simular N rodadas")
    print("4 - Mostrar fila")
    print("5 - Mostrar próximo a jogar")
    print("6 - Limpar fila")
    print("7 - Sair")

    opcao = int(input("Digite sua opção: "))
    return opcao


def main():
    fila = None
    opcao = 0

    while opcao != 7:

        opcao = menu()

        if opcao == 1:
            jogador = input("Digite o nome do jogador: ")
            fila = inserir(fila, jogador)

        elif opcao == 2:
            fila = rodada(fila)

        elif opcao == 3:
            quantidade = int(input("Digite a quantidade de rodadas: "))

            for i in range(quantidade):
                print()
                print("Rodada", i + 1)

                fila = rodada(fila)

                print("Fila:")
                listar(fila)

        elif opcao == 4:
            print()
            print("Fila de jogadores:")
            listar(fila)

        elif opcao == 5:
            if fila == None:
                print("Fila vazia")
            else:
                print("Próximo a jogar:", fila.dado)

        elif opcao == 6:
            fila = None
            print("Fila limpa")

        elif opcao == 7:
            print("Encerrando...")

        else:
            print("Erro, tente novamente")


main()
