class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def inserir_cabeca(self, dado):
        no = No(dado)

        if self.head == None:
            self.head = self.tail = no
            return

        no.proximo = self.head
        self.head.anterior = no
        self.head = no

    def inserir_cauda(self, dado):
        no = No(dado)

        if self.tail == None:
            self.head = self.tail = no
            return

        no.anterior = self.tail
        self.tail.proximo = no
        self.tail = no

    def excluir_cabeca(self):
        if self.head == None:
            print("Fila de chamados vazia!")
            return

        print("Chamado atendido:", self.head.dado)

        if self.head == self.tail:
            self.head = self.tail = None
            return

        self.head = self.head.proximo
        self.head.anterior = None

    def excluir_cauda(self):
        if self.tail == None:
            print("Fila de chamados vazia!")
            return

        print("Chamado atendido:", self.tail.dado)

        if self.head == self.tail:
            self.head = self.tail = None
            return

        self.tail = self.tail.anterior
        self.tail.proximo = None

    def mostrar_cabeca(self):
        if self.head == None:
            print("Fila de chamados vazia!")
            return

        aux = self.head

        print("Chamados na fila:")

        while aux != None:
            print("-", aux.dado)
            aux = aux.proximo

    def mostrar_cauda(self):
        if self.tail == None:
            print("Fila de chamados vazia!")
            return

        aux = self.tail

        print("Chamados na ordem inversa:")

        while aux != None:
            print("-", aux.dado)
            aux = aux.anterior


def menu():
    print("1 - Adicionar chamado comum")
    print("2 - Adicionar chamado urgente")
    print("3 - Atender chamado do inicio")
    print("4 - Atender chamado do fim")
    print("5 - Listar chamados")
    print("6 - Sair")
    opcao = int(input("Digite sua opcao: "))
    return opcao


def main():
    deque = Deque()
    opcao = 0

    while opcao != 6:
        opcao = menu()

        if opcao == 1:
            chamado = input("Digite o chamado: ")
            deque.inserir_cauda(chamado)

        elif opcao == 2:
            chamado = input("Digite o chamado urgente: ")
            deque.inserir_cabeca(chamado)

        elif opcao == 3:
            deque.excluir_cabeca()

        elif opcao == 4:
            deque.excluir_cauda()

        elif opcao == 5:
            deque.mostrar_cabeca()

        elif opcao == 6:
            print("Encerrando o sistema...")

        else:
            print("Opcao invalida!")


main()
