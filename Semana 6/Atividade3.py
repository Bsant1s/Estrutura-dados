class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


def inserir(pilha, dado):
    no = No(dado)

    if pilha == None:
        pilha = no
        return pilha

    no.proximo = pilha
    pilha = no

    return pilha


def listar(pilha):
    aux = pilha
    contador = 1

    if pilha == None:
        print("Garagem vazia")
        return

    while aux != None:
        print(contador, "-", aux.dado)
        aux = aux.proximo
        contador = contador + 1


def remover(pilha):
    if pilha == None:
        print("Garagem vazia")
        return None

    return pilha.proximo


def menu():
    print()
    print("1 - Listar carros")
    print("2 - Escolher carro para retirar")
    print("3 - Sair")

    opcao = int(input("Digite sua opção: "))

    return opcao


def main():
    pilha = None

    # Cadastro dos 20 carros
    print("CADASTRO DOS 20 CARROS")
    print()

    for i in range(20):
        carro = input("Digite o nome do carro: ")
        pilha = inserir(pilha, carro)

    print()
    print("Carros cadastrados:")
    listar(pilha)

    opcao = 0

    while opcao != 3:
        opcao = menu()

        if opcao == 1:
            listar(pilha)

        elif opcao == 2:
            carro_escolhido = input("Digite o carro que deseja retirar: ")

            aux = pilha
            encontrado = False

            while aux != None:
                if aux.dado == carro_escolhido:
                    encontrado = True
                    break
                aux = aux.proximo

            if encontrado == False:
                print("Carro não encontrado")

            else:
                print()
                print("Carros retirados:")

                while pilha.dado != carro_escolhido:
                    print(pilha.dado)
                    pilha = remover(pilha)
                    
                print(pilha.dado)
                pilha = remover(pilha)

        elif opcao == 3:
            print("Encerrando...")

        else:
            print("Erro, tente novamente")


main()
