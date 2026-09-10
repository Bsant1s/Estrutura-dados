class No:
    def __init__(self, nome, idade, prioridade):
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade
        self.proximo = None
        self.anterior = None


def inserir(lista, nome, idade, prioridade):
    novo = No(nome, idade, prioridade)

    if lista is None:
        novo.proximo = novo
        novo.anterior = novo
        return novo

    novo.proximo = lista
    novo.anterior = lista.anterior
    lista.anterior.proximo = novo
    lista.anterior = novo

    return lista


def mostrar(lista):
    if lista is None:
        print("Nenhum paciente")
        return

    atual = lista

    while True:
        print("Nome:", atual.nome)
        print("Idade:", atual.idade)
        print("Prioridade:", atual.prioridade)

        if atual.proximo == lista:
            return

        atual = atual.proximo


def retirar(lista, nome):
    if lista is None:
        print("Nenhum paciente na fila")
        return lista
    atual = lista

    while True:
        if atual.nome == nome:

            if atual.proximo == atual:
                return None

            elif atual == lista:
                lista.proximo.anterior = lista.anterior
                lista.anterior.proximo = lista.proximo
                lista = lista.proximo
                return lista

            else:
                atual.proximo.anterior = atual.anterior
                atual.anterior.proximo = atual.proximo
                return lista

        elif atual.proximo == lista:
            print("Erro, paciente não encontrado")
            return lista

        atual = atual.proximo


def atender(lista):

    if lista is None:
        print("Não há pacientes na fila")
        return lista
    atual = lista

    while True:
        if atual.prioridade == "Emergência":
            print("Atendendo:", atual.nome)
            print("Prioridade:", atual.prioridade)
            lista = retirar(lista, atual.nome)
            return lista

        if atual.proximo == lista:
            break

        atual = atual.proximo
    atual = lista

    while True:
        if atual.prioridade == "Urgente":
            print("Atendendo:", atual.nome)
            print("Prioridade:", atual.prioridade)
            lista = retirar(lista, atual.nome)
            return lista

        if atual.proximo == lista:
            break

        atual = atual.proximo
    atual = lista

    while True:
        if atual.prioridade == "Normal":
            print("Atendendo:", atual.nome)
            print("Prioridade:", atual.prioridade)
            lista = retirar(lista, atual.nome)
            return lista

        if atual.proximo == lista:
            break

        atual = atual.proximo

    print("Erro, tente novamente")
    return lista


def main():
    lista = None

    quantidade = int(input("Digite a quantidade de pacientes: "))
    for contador in range(quantidade):
        nome = input("Digite o nome do paciente: ")
        idade = int(input("Digite a idade: "))

        print("1 - Emergência")
        print("2 - Urgente")
        print("3 - Normal")
        opcao = int(input("Digite a prioridade: "))

        if opcao == 1:
            prioridade = "Emergência"
        elif opcao == 2:
            prioridade = "Urgente"
        else:
            prioridade = "Normal"

        lista = inserir(lista, nome, idade, prioridade)

    print("Pacientes na fila:")
    mostrar(lista)

    while lista is not None:
        lista = atender(lista)

    print("Todos os pacientes foram atendidos.")

main()

