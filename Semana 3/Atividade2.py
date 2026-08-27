class No:
    def __init__(self, nome, identificador):
        self.nome = nome
        self.identificador = identificador
        self.proximo = None
        self.anterior = None

def inserir (lista, nome, identificador):
    novo = No(nome, identificador)

    if lista is None:
        return novo

    atual = lista

    while atual.proximo is not None:
        atual = atual.proximo

    atual.proximo = novo
    novo.anterior = atual

    return lista

def listar(lista):
    if lista is None:
        print("Lista vazia")
        return 
    atual = lista

    while atual is not None:
        print("Nome:", atual.nome)
        print("Identificador:", atual.identificador)
        atual = atual.proximo

def remover (lista, identificador):
    if lista is None:
      print("Lista vazia")
      return lista

    atual = lista

    while atual is not None:
        if atual.identificador == identificador:
            if atual.anterior is None:
                lista = atual.proximo

            if lista is not None:
                lista.anterior = None

        else:
          atual.anterior.proximo = atual.proximo

          if atual.proximo is not None:
            atual.proximo.anterior = atual.anterior

        print("Nó removido")
        return lista
      
    atual = atual.proximo

    print("Erro, tente novamente")
    return lista   

def buscar_nome(lista, nome):
    atual = lista

    while atual is not None:

        if atual.nome == nome:
            print("Nó encontrado!")
            print("Nome:", atual.nome)
            print("Identificador:", atual.identificador)
            return

        atual = atual.proximo

    print("Nome não encontrado!")

def buscar_identificador(lista, identificador):
    atual = lista

    while atual is not None:

        if atual.identificador == identificador:
            print("Nó encontrado!")
            print("Nome:", atual.nome)
            print("Identificador:", atual.identificador)
            return

        atual = atual.proximo

    print("Erro, tente novamente")

def main():

    lista = None

    while True:

        print("1 - Inserir nó")
        print("2 - Listar nós")
        print("3 - Remover nó")
        print("4 - Verificar se nó existe")
        print("5 - Sair")
        opcao = int(input("Digite a sua opção: "))

        if opcao == 1:

            nome = input("Digite o nome: ")
            identificador = int(input("Digite o identificador: "))

            lista = inserir(lista, nome, identificador)

            print("Nó inserido!")

        elif opcao == 2:
            listar(lista)

        elif opcao == 3:

            identificador = int(input("Digite o identificador do nó que deseja remover: "))
            lista = remover(lista, identificador)

        elif opcao == 4:

            print("1 - Buscar por nome")
            print("2 - Buscar por identificador")
            busca = int(input("Digite a sua opção: "))

            if busca == 1:
                nome = input("Digite o nome: ")
                buscar_nome(lista, nome)

            elif busca == 2:
                identificador = int(input("Digite o identificador: "))
                buscar_identificador(lista, identificador)

            else:
                print("Erro, tente novamente!")

        elif opcao == 5:

            print("Encerrando...")
            break

        else:
            print("Erro, tente novamente!")


main()
