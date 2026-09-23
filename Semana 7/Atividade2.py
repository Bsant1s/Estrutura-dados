class NoDuplo:
    def __init__(self, nome):
        self.nome = nome
        self.anterior = None
        self.proximo = None


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None

    def adicionar_inicio(self, nome):
        novo = NoDuplo(nome)

        if self.inicio is None:
            self.inicio = novo
        else:
            novo.proximo = self.inicio
            self.inicio.anterior = novo
            self.inicio = novo

    def percorrer_frente(self):
        aux = self.inicio

        while aux is not None:
            print(aux.nome)
            aux = aux.proximo

    def percorrer_tras(self):
        aux = self.inicio

        while aux.proximo is not None:
            aux = aux.proximo

        while aux is not None:
            print(aux.nome)
            aux = aux.anterior


def main():
    lista = ListaDuplamenteEncadeada()

    lista.adicionar_inicio("Patrícia")
    lista.adicionar_inicio("Elizanete")
    lista.adicionar_inicio("Carol")
    lista.adicionar_inicio("Fabiana")

    print("Primeiro ao último:")
    lista.percorrer_frente()

    print()

    print("Último ao primeiro:")
    lista.percorrer_tras()


main()
