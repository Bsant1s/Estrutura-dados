class No:
    def __init__(self, parada):
        self.parada = parada
        self.proximo = None
        self.anterior = None

def inserir(lista, parada):
    no = No(parada)

    if lista is None:
        no.proximo = no
        no.anterior = no
        lista = no
        return lista
    no.proximo = lista
    no.anterior = lista.anterior
    lista.anterior.proximo = no
    lista.anterior = no

    lista = no
    return lista

def listar (lista):
    if lista is None:
        print("Lista vazia")
        return lista

    aux = lista

    while True:
        print("-", aux.parada)
        if aux.proximo == lista:
            return lista 
        aux = aux.proximo

def excluir(lista, parada):
    aux = lista

    if lista is None:
        print("Lista vazia")
        return lista

    while True:
        if aux.parada == parada:

            if aux.proximo.anterior == aux:
                print("Único elemento da lista")
                return None
            elif aux == lista:  #cabeça da lista
                lista.proximo.anterior = lista.anterior 
                lista.anterior.proximo = lista.proximo
                lista = lista.proximo
                return lista
            else: #quando está no meio, mesmo processo do anterior, mas com aux
                aux.proximo.anterior  = aux.anterior
                aux.anterior.proximo = aux.proximo
                return lista

        elif aux.proximo == lista:
            print("Dado não encontrado")
            return lista
        aux = aux.proximo

def simular (lista, quantidade):
    if lista is None:
        print("Lista vazia")
        return 

    aux = lista
    for i in range (quantidade):
        print("Percurso:", i + 1)
        print("Parada:", aux.parada)
        aux = aux.proximo

def menu():
    print("1 - Adicionar parada")
    print("2 - Listar paradas")
    print("3 - Remover parada")
    print("4 - Simular percurso")
    print("5 - Sair")
    opcao = int(input("Digite sua opção:"))
    return opcao 

def main():
    lista = None
    opcao = 0

    while opcao != 5:
        opcao = menu()
        if opcao == 1:
            parada = input("Digite o nome da parada:")
            lista = inserir(lista, parada)

        elif opcao == 2:
            listar(lista)

        elif opcao == 3:
            parada = input("Digite a parada que deseja remover:")
            lista = excluir (lista, parada)

        elif opcao == 4:
            quantidade = int(input("Quantas paradas deseja percorrer:"))
            simular(lista, quantidade)

        elif opcao == 5:
            print("Encerrando...")

        else:
            print("Erro, tente novamnete")

main()
