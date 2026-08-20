class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def menu ():
    print("1 - Inserir item")
    print("2 - Listar itens")
    print("3 - Remover item")
    print("4 - Maiores")
    print("5 - Último da lista")
    print("6 - Inserir no final")
    print("7 - Média dos valores")
    print("8 - Alterar sinais")
    opcao = int(input("Digite a sua opção:"))
    return opcao

def inserir (valor,lista):
    no = No(valor)

    if lista == None:
       lista = no
    else:
        atual = lista

        while atual.proximo != None:
            atual = atual.proximo

        atual.proximo = no
    return lista

def listar(lista):
    if lista == None:
        print("Lista vazia")
    else:
        atual = lista

        while atual != None:
            print(atual.valor)
            atual = atual.proximo

    
def remover(lista, valor):
    if lista == None:
        print("Lista vazia")
        return lista
    if lista.valor == valor:
        lista = lista.proximo
        return lista

    atual = lista
    while atual.proximo != None:
        if atual.proximo.valor == valor:
            atual.proximo = atual.proximo.proximo
            return lista

        atual = atual.proximo

    print("Valor não encontrado")
    return lista

def maiores(lst, n):
    contador = 0

    while lst != None:
        if lst.valor > n:
            contador += 1

        lst = lst.proximo

    return contador

def ultimo (lista):
    if lista == None:
        return None

    atual = lista

    while atual.proximo != None:
        atual = atual.proximo

    return atual

def final(lst, valor):
    no = No (valor)

    if lst == None:
        lst = no
    else:
        atual = lst

        while atual.proximo != None:
            atual = atual.proximo

        atual.proximo = no

    return lst

def calcular_media (lst):
    if lst == None:
        return 0

    soma = 0
    quantidade = 0

    atual = lst

    while atual != None:
        soma = soma + atual.valor
        quantidade += 1
        atual = atual.proximo

    media = soma / quantidade
    return media

def lista_altera(lst):
    atual = lst

    while atual != None:
        atual.valor = atual.valor * -1
        atual = atual.proximo

    return lst

def main():
    lista = None

    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input("Digite um valor:"))
            lista = inserir(valor, lista)

        elif opcao == 2:
            listar(lista)

        elif opcao == 3:
            valor = float(input("Digite o valor que deseja remover:"))
            lista = remover(lista, valor)

        elif opcao == 4:
            n = float(input("Digite um número:"))
            quantidade = maiores (lista,n)
            print("Quantidade de valores maiores:", quantidade)

        elif opcao == 5:
            no = ultimo(lista)

            if no == None:
                print("Lista vazia")
            else:
                print("Último valor da lista:", no.valor)

        elif opcao == 6:
            valor = float(input("Digite o valor para adicionar:"))
            lista = final(lista, valor)

        elif opcao == 7:
            media = calcular_media (lista)
            print("Média dos valores:", media)

        elif opcao == 8:
            lista = lista_altera(lista)
            print("Valores modificador")

        else:
            print("Opção inválida, tente novamente...")

main()
