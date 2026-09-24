class NoDuploCircular:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None


class ListaDuplamenteEncadeadaCircular:
    def __init__(self):
        self.inicio = None

    def adicionar_inicio(self, dado):
        no = NoDuploCircular(dado)

        if self.inicio is None:
            no.proximo = no
            no.anterior = no
            self.inicio = no
        else:
            ultimo = self.inicio.anterior

            no.proximo = self.inicio
            no.anterior = ultimo

            ultimo.proximo = no
            self.inicio.anterior = no

            self.inicio = no

    def adicionar_final(self, dado):
        no = NoDuploCircular(dado)

        if self.inicio is None:
            no.proximo = no
            no.anterior = no
            self.inicio = no
        else:
            ultimo = self.inicio.anterior

            no.proximo = self.inicio
            no.anterior = ultimo

            ultimo.proximo = no
            self.inicio.anterior = no

    def percorrer_frente(self, quantidade):
        if self.inicio is None:
            print("Lista vazia")
            return

        aux = self.inicio
        for i in range(quantidade):
            print(aux.dado)
            aux = aux.proximo

    def percorrer_tras(self, quantidade):
        if self.inicio is None:
            print("Lista vazia")
            return

        aux = self.inicio.anterior

        for i in range(quantidade):
            print(aux.dado)
            aux = aux.anterior

    def remover(self, dado):
        if self.inicio is None:
            print("Lista vazia")
            return

        aux = self.inicio

        while True:
            if aux.dado == dado:

                if aux.proximo == aux:
                    self.inicio = None

                else:
                    aux.anterior.proximo = aux.proximo
                    aux.proximo.anterior = aux.anterior

                    if aux == self.inicio:
                        self.inicio = aux.proximo
                return
            aux = aux.proximo
            if aux == self.inicio:
                break

        print("Elemento não encontrado")

def main():
    lista = ListaDuplamenteEncadeadaCircular()

    lista.adicionar_inicio("A")
    lista.adicionar_inicio("B")
    lista.adicionar_inicio("C")

    print("Lista do início:")
    lista.percorrer_frente(3)

    print()
    lista.adicionar_final("D")
    lista.adicionar_final("E")

    print("Para frente:")
    lista.percorrer_frente(5)

    print()

    print("Para trás:")
    lista.percorrer_tras(5)

    print()
    print("Removendo B:")
    lista.remover("B")

    print()
    print("Lista após remover (para frente):")
    lista.percorrer_frente(6)

    print()

    print("Lista após remover (para trás):")
    lista.percorrer_tras(6)

main()
