class No:
    def __init__(self, nome, responsavel):
        self.nome = nome
        self.responsavel = responsavel
        self.proximo = None


def inserir(lista, nome, responsavel):
    no = No(nome , responsavel)

    if lista is None:
        lista = no
        return lista

    else:
        aux = lista

        while aux.proximo is not None:
            aux = aux.proximo
        aux.proximo = no
        return lista

def listar(lista):
    aux = lista

    while aux is not None:
        print(aux.nome)
        print(aux.responsavel)
        aux = aux.proximo


def remover(lista, nome):
    aux = lista

    if lista is None:
        print("Lista vazia")
        return lista
    
    if lista.nome == nome:
        lista = lista.proximo 
        return lista

    aux = lista

    while aux.proximo is not None  and aux.proximo.nome != nome:
        aux = aux.proximo

    if aux.proximo is not None:
        aux.proximo = aux.proximo.proximo
    return lista


lista = None
lista = inserir(lista, "- Planejamento do Produto:", "Ana")
lista = inserir(lista, "- Implementação do Backend:", "João")
lista = inserir(lista, "- Testes:", "Carla")

print("Sprints cadastradas:")
listar(lista)
print()
print("Após remoção:")
lista = remover(lista, "- Planejamento do Produto:")
listar (lista)
