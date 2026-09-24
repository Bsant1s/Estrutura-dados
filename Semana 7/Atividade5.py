class Fila:
    def __init__(self):
        self.elementos = []

    def enfileirar(self, usuario):
        self.elementos.append(usuario)

    def desenfileirar(self):
        if len(self.elementos) > 0:
            return self.elementos.pop(0)
        else:
            print("A fila está vazia.")

    def percorrer(self):
        for usuario in self.elementos:
            print(usuario)

    def frente(self):
        if len(self.elementos) > 0:
            return self.elementos[0]
        else:
            print("A fila está vazia.")

    def esta_vazia(self):
        return len(self.elementos) == 0

    def tamanho(self):
        return len(self.elementos)


def calcular_media(fila):
    if fila.esta_vazia():
        return 0

    soma = 0

    for tempo in fila.elementos:
        soma = soma + tempo

    media = soma / fila.tamanho()

    return media


def main():
    fila = Fila()

    while True:
        print("\n--- MENU ---")
        print("1 - Adicionar usuário")
        print("2 - Atender usuário")
        print("3 - Mostrar fila")
        print("4 - Mostrar próximo usuário")
        print("5 - Verificar se a fila está vazia")
        print("6 - Mostrar tamanho da fila")
        print("7 - Calcular tempo médio de espera")
        print("8 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            usuario = input("Digite o nome do usuário: ")
            fila.enfileirar(usuario)
            print("Usuário adicionado!")

        elif opcao == 2:
            usuario = fila.desenfileirar()

            if usuario is not None:
                print("Usuário atendido:", usuario)

        elif opcao == 3:
            print("\nUsuários aguardando atendimento:")
            fila.percorrer()

        elif opcao == 4:
            usuario = fila.frente()

            if usuario is not None:
                print("Próximo usuário:", usuario)

        elif opcao == 5:
            if fila.esta_vazia():
                print("A fila está vazia.")
            else:
                print("Existem usuários aguardando.")

        elif opcao == 6:
            print("Quantidade de usuários:", fila.tamanho())

        elif opcao == 7:
            print("Para calcular a média, a fila deve conter tempos de espera.")

        elif opcao == 8:
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


main()
