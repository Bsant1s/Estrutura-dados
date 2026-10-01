class No:
    def __init__(self, nome, duracao, ambiente, ativo):
        self.nome = nome 
        self.duracao = duracao 
        self.ambiente = ambiente
        self.ativo = ativo
        self.proximo = None

        
def adicionar (lista, nome, duracao, ambiente, ativo):
    no = No(nome, duracao, ambiente, ativo)

    if lista is None:
        lista = no
        no.proximo = no
        return lista 

    aux = lista
    while aux.proximo != lista:
        aux = aux.proximo 

        aux.proximo = no  
        no.proximo = lista

        return lista

def listar (lista, nome):
    aux = lista

    while True:
        print(aux.nome)
        print(aux.duracao)
        print(aux.ambiente)
        print(aux.ativo)

        aux = aux.proximo

        if aux == lista:
            break

def listar_ambiente(lista):
    if lista is None:
        print("Lista vazia")
        return lista

    ambientes = ["testes", "homologação", "produção"]

    for ambiente in ambientes:
        aux = lista

        while True:
            if aux.ambiente == ambiente:
                print(aux.nome)
                print(aux.duracao)
                print(aux.ambiente)
                print(aux.ativo)

                aux = aux.proximo

                if aux == lista:
                    break

def listar_ativos (lista):
    aux  = lista

    if lista is None:
        print("Lista vazia")
        return lista

    while True:
        if aux.ativo == True:
            print(aux.nome)
            print(aux.duracao)
            print(aux.ambiente)
            print(aux.ativo)

        aux = aux.proximo

        if aux == lista:
            break

def tempo(lista, ):
    if lista is None:
        print("Lista vazia")
        return lista 
    
    total = 0
    aux = lista

    while True:
      total = total + aux.duracao
      aux = aux.proximo
      if aux == lista:
          break
    print("Tempo total de duração:", total)

def ativar (lista, nome):
    if lista is None:
        print("Lista vazia")
        return lista
    
    aux = lista 

    while True:
        if aux.nome == nome:
            aux.ativo = True
            return lista

        aux = aux.proximo
        if aux == lista:
            print("Deploy não encontrado")
            return lista 

def desativar(lista, nome):
       if lista is None:
           print("Lista vazia")
           return lista
    
       aux = lista 

       while True:
        if aux.nome == nome:
            aux.ativo = False
            return lista

        aux = aux.proximo
        if aux == lista:
            print("Deploy não encontrado")
            return lista 

def remover (lista, nome):
    if lista is None:
        print("Lista vazia")
        return lista

    if lista.nome == nome and lista.proximo == lista:
        lista = None
        return lista 

    aux = lista
    while aux.proximo != lista and aux.proximo.nome != nome:
        aux.proximo = aux.proximo.proximo

    if aux.proximo == lista:
        print("Deploy não encontrado")
        return lista


def main():
    lista = None

    while True:
        print("1 - Adicionar deploy")
        print("2 - Listar todos os deploys")
        print("3 - Listar por ambiente")
        print("4 - Listar apenas os ativos")
        print("5 - Exibir tempo total")
        print("6 - Ativar deploy")
        print("7 - Desativar deploy")
        print("8 - Excluir deploy")
        print("9 - Sair")

        opcao = int(input("Digite uma opção: "))

        if opcao == 1:
            nome = input("Nome do deploy: ")
            duracao = int(input("Duração em segundos: "))
            ambiente = input("Ambiente (teste/homologação/produção): ")
            ativo = input("O deploy está ativo? (s/n): ")

            if ativo == "s":
                ativo = True
            else:
                ativo = False

            lista = adicionar(lista, nome, duracao, ambiente, ativo)

        elif opcao == 2:
            listar(lista)

        elif opcao == 3:
            listar_ambiente(lista)

        elif opcao == 4:
            listar_ativos(lista)

        elif opcao == 5:
            tempo(lista)

        elif opcao == 6:
            nome = input("Digite o nome do deploy que deseja ativar: ")
            lista = ativar(lista, nome)

        elif opcao == 7:
            nome = input("Digite o nome do deploy que deseja desativar: ")
            lista = desativar(lista, nome)

        elif opcao == 8:
            nome = input("Digite o nome do deploy que deseja excluir: ")
            lista = remover(lista, nome)

        elif opcao == 9:
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")


main()
