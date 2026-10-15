
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

    def atender(self):
        if self.head == None:
            print("Fila vazia!")
            return

        print("Cliente atendido:", self.head.dado)

        if self.head == self.tail:
            self.head = self.tail = None
            return

        self.head = self.head.proximo
        self.head.anterior = None

    def mostrar(self):
        if self.head == None:
            print("Fila vazia!")
            return

        aux = self.head

        print("Ordem atual de atendimento:")

        while aux != None:
            print("-", aux.dado)
            aux = aux.proximo


def menu():
    print("1 - Adicionar cliente comum")
    print("2 - Adicionar cliente preferencial")
    print("3 - Atender cliente")
    print("4 - Mostrar fila")
    print("5 - Sair")
    opcao = int(input("Digite sua opcao: "))
    return opcao


def main():
    deque = Deque()
    opcao = 0

    while opcao != 5:
        opcao = menu()

        if opcao == 1:
            nome = input("Nome do cliente comum: ")
            deque.inserir_cauda(nome)

        elif opcao == 2:
            nome = input("Nome do cliente preferencial: ")
            deque.inserir_cabeca(nome)

        elif opcao == 3:
            deque.atender()
            deque.mostrar()

        elif opcao == 4:
            deque.mostrar()

        elif opcao == 5:
            print("Encerrando o sistema...")

        else:
            print("Opcao invalida!")


main()
