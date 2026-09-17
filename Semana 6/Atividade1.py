class No:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None
        self.anterior = None


def inserir(fila_inicio, fila_fim, nome):
    novo = No(nome)

    if fila_inicio is None:
        fila_inicio = novo
        fila_fim = novo
        return fila_inicio, fila_fim

    fila_fim.proximo = novo
    novo.anterior = fila_fim
    fila_fim = novo
    return fila_inicio, fila_fim


def listar(fila_inicio):
    aux = fila_inicio
    contador = 1

    if fila_inicio is None:
        print("Fila vazia")
        return

    while aux is not None:
        print(contador, "-", aux.nome)
        contador += 1
        aux = aux.proximo


def remover(fila_inicio, fila_fim):
    if fila_inicio is None:
        print("Fila vazia")
        return None, None

    print("Chamado atendido:", fila_inicio.nome)

    if fila_inicio == fila_fim:
        return None, None

    fila_inicio = fila_inicio.proximo
    fila_inicio.anterior = None

    return fila_inicio, fila_fim


def quantidade(fila_inicio):
    contador = 0
    aux = fila_inicio

    while aux is not None:
        contador += 1
        aux = aux.proximo

    return contador


def proximo(fila_inicio):
    if fila_inicio is None:
        print("Fila vazia")
    else:
        print("Próximo chamado:", fila_inicio.nome)


def menu():
    print("1 - Registrar chamado")
    print("2 - Listar chamados")
    print("3 - Atender chamado")
    print("4 - Mostrar quantidade de chamados")
    print("5 - Mostrar próximo chamado")
    print("6 - Sair")

    opcao = int(input("Digite sua opção: "))
    return opcao


def main():
    opcao = 0
    fila_inicio = None
    fila_fim = None

    while opcao != 6:
        opcao = menu()

        if opcao == 1:
            nome = input("Digite o nome da pessoa: ")
            fila_inicio, fila_fim = inserir(fila_inicio, fila_fim, nome)

        elif opcao == 2:
            listar(fila_inicio)

        elif opcao == 3:
            fila_inicio, fila_fim = remover(fila_inicio, fila_fim)

        elif opcao == 4:
            total = quantidade(fila_inicio)
            print("Chamados aguardando:", total)

        elif opcao == 5:
            proximo(fila_inicio)

        elif opcao == 6:
            print("Encerrando...")

        else:
            print("Erro, tente novamente")


main()
