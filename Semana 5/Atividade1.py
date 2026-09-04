class No:
    def __init__(self, id):
        self.bastao = False
        self.id = id
        self.proximo = None

def adicionar(lista, id):
    novo = No(id)

    if lista is None:
        novo.proximo = novo
        return novo

    aux = lista

    while aux.proximo != lista:
        aux = aux.proximo

    aux.proximo = novo
    novo.proximo = lista
    return lista

def remover (lista, id):
    if lista is None:
        print("Lista vazia")
        return lista
    aux = lista
    anterior = None

    while True:
        if aux.id == id:
            if aux.proximo == lista:
                return None
            elif aux == lista:
                ultimo = lista

                while ultimo.proximo != lista:
                    ultimo = ultimo.proximo

                lista = lista.proximo
                ultimo.proximo = lista
            else:
                anterior.porximo = aux.proximo
            return lista
        anterior = aux
        aux = aux.proximo

        if aux == lista:
            break
    print("Atleta não encontrado, tente novamente")
    return lista

def listar(lista):
    if lista is None:
        print("Lista vazia")
        return 

    aux = lista
    while True:
        print("Atleta:", aux.id, "- Bastão", aux.bastao)
        aux = aux.proximo
        if aux == lista:
            break

def simular (lista, quantidade):
    if lista is None:
        print("Lista vazia")
        return 

    aux = lista
    aux.bastao = True
    for i in range (quantidade):
        print("Turno:", i+1)
        print("Atleta:", aux.id)
        print("Está com o bastão")

        aux.bastao = False
        aux = aux.proximo
        aux.bastao = True

lista = None

quantidade = int(input("Quantos atletas deseja cadastrar??"))
for i in range (quantidade):
    id = int(input("Digite o id do atleta:"))
    lista = adicionar(lista, id)

print("Todos os atletas cadastrados:")
listar(lista)

print("Simulação:")
turnos = int(input("Quantos turnos quer simular:"))
simular(lista, turnos)

print("Remover atleta:")
id = int(input("Digite o id do atleta que deseja remover:"))
lista = remover(lista, id)

print("Lista atual:")
listar(lista)
