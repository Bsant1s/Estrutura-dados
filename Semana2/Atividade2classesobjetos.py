class Contabancaria:
    def __init__(self, nome, numero, saldo):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo

    def consultar_saldo(self):
        print("Nome do tirular:", self.nome)
        print("Número de acesso:", self.numero)
        print("Saldo:", self.saldo)

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Valor depositado")
        else:
            print("Erro, tente novamente")

    def sacar (self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print("Saque realizado!")
            else:
                print("Saldo insuficiente")
        else:
            print("Erro, tente novamente")

    def transferir (self, valor, outra_conta):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                outra_conta.saldo += valor
                print("Transferência concluida")
            else:
              print("Saldo insuficiente")

        else:
            print("Erro, tente novamente")

def main():
    nome1 = input("Digite o nome do titular:")
    numero1 = int(input("Digite o número da conta:"))
    saldo1 = float(input("Digite o saldo:"))
    conta1 = Contabancaria(nome1, numero1, saldo1)

    nome2 = input("Digite o nome do titular:")
    numero2 = int(input("Digite o número da conta:"))
    saldo2 = float(input("Digite o saldo:"))
    conta2 = Contabancaria(nome2, numero2, saldo2)

    while True:
        print("1 - Consultar saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Transferir")
        print("5 - Sair")
        opcao = int(input("Digite a opção;"))

        if opcao == 1:
            print("Primeira conta:")
            conta1.consultar_saldo()
            print("Segunda conta:")
            conta2.consultar_saldo()

        elif opcao == 2:
            print("Primeira conta:",  conta1.nome)
            print("Segunda conta:", conta2.nome)

            conta = int(input("Digite o número da conta"))
            valor = float(input("Digite o valor do depósito:"))

            if conta == 1:
                conta1.depositar(valor)

            elif conta == 2:
                conta2.depositar(valor)

            else:
                print("Conta não encontrada")

        elif opcao == 3:
            print("Primeira conta:",  conta1.nome)
            print("Segunda conta:", conta2.nome)
            
            conta = int(input("Digite o número da conta"))
            valor = float(input("Digite o valor do saque:"))
            
            if conta == 1:
              conta1.sacar(valor)
            
            elif conta == 2:
              conta2.sacar(valor)
            
            else:
              print("Conta não encontrada")

        elif opcao == 4:
            print("Primeira conta:",  conta1.nome)
            print("Segunda conta:", conta2.nome)

            origem = int(input("Digite a conra de origem:"))

            print("Primeira conta:",  conta1.nome)
            print("Segunda conta:", conta2.nome)

            destino = int(input("Digite a conta de destino:"))

            valor = float(input("Digite o valor da transferência:"))

            if origem == 1 and destino == 2:
                conta1.transferir (valor, conta2)
            elif origem == 2 and destino == 1:
                conta2.transferir (valor, conta1)
            else:
                print("Conta inválida")

        elif opcao == 5:
            print("encerrando...")
            break
    else:
       print("Erro tente novamente")
main()
