import random

class No:
    def __init__(self, guerreiro):
        self.guerreiro = guerreiro
        self.proximo = None
        self.anterior  = None

def inserir (lista, guerreiro):
    novo = No(guerreiro)

    if lista is None:
        novo.proximo = novo
        novo.anterior = novo
        lista = novo
        return novo

    novo.proximo = lista
    novo.anterior = lista.anterior
    lista.anterior.proximo = novo
    lista.anterior = novo
    return lista


def mostrar(lista):
    primeiro = lista

    if lista is None:
        print("Nenhum guerreiro na roda")
        return 
    while True:
        print("-", primeiro.guerreiro)
        if primeiro.proximo == lista:
            return
        primeiro = primeiro.proximo

def eliminar (lista, guerreiro):
    atual = lista
    if lista is None:
        return lista

    while True:
        if atual.guerreiro == guerreiro:
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
            return lista
        
        atual = atual.proximo

def jogar(quantidade):
    lista = None
    for numero in range (1, quantidade + 1):
        lista = inserir(lista, numero)
        print("Guerreiros participantes:")
        mostrar(lista)
        restante = quantidade

    while restante > 1:
            sorteio = random.randint(1, restante)
            atual = lista
            for contador in range (1, sorteio):
                atual = atual.proximo
            print("Guerreiro eliminado:", atual.guerreiro)
            lista = eliminar (lista, atual.guerreiro)
            restante = restante - 1
    print("Guerreiro sobrevivente:", lista.guerreiro)

def main ():
    quantidade = int(input("Digite a quantidade de guerreiros:"))
    if quantidade < 2:
        print("Digite no mínimo 2 guerreiros:")
    else:
        jogar(quantidade)

main()
            
