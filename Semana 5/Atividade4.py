class No:
    def __init__(self, cliente):
        self.cliente = cliente
        self.proximo = None
        self.anterior = None

def inserir(lista, cliente):
    novo = No(cliente)

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
    atual = lista

    if lista is None:
        print("Nenhum cliente no rodízio")
        return

    while True:
        print("-", atual.cliente)

        if atual.proximo == lista:
            return
        atual = atual.proximo


def retirar(lista, cliente):
    atual = lista
    if lista is None:
        print("Rodízio vazio")
        return lista

    while True:

        if atual.cliente == cliente:

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
            print("Cliente não encontrado")
            return lista

        atual = atual.proximo


def passar_pizza(lista, quantidade):
    atual = lista

    if lista is None:
        print("Nenhum cliente com a pizza")
        return

    for contador in range(quantidade):
        print("Cliente que está com a pizza:", atual.cliente)
        atual = atual.proximo


def main():
    lista = None
    quantidade = int(input("Digite a quantidade de pessoas:"))
    for contador in range (quantidade):

        cliente = input("Digite o nome do cliente:")
        lista = inserir(lista, cliente)

    print("Clientes no rodízio:")
    mostrar(lista)

    quantidade = int(input("Digite a quantidade de vezes que a pizza vai passar:"))
    print("Passagem de pizza:")
    passar_pizza (lista, quantidade)
    cliente = input("Digite o nome do cliente que saio:")
    lista = retirar(lista, cliente)
    print("Clientes:")
    mostrar(lista)

    quantidade = int(input("Quantas vezes a pizza vai passar?"))
    print("Nova passagem de pizza:")
    passar_pizza(lista, quantidade)

  
main()
