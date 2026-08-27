class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade 

    def exibir(self):
      print("Produto:", self.nome)
      print("Preço:", self.preco)
      print("Quantidade:", self.quantidade)
      print("valor do estoque:", self.preco * self.quantidade)


    def adicionar (self, quantidade):
      self.quantidade += quantidade

    def vender (self, quantidade):
      if quantidade <= self.quantidade:
        self.quantidade -=quantidade
        print("venda realizada")

      else:
        print("Erro, tente novamente")
        print("Quantidade maior que estoque")

    def valor_estoque (self):
      return self.preco * self.quantidade


def main():

    nome1 = input("Digite o nome:")
    preco1 = float(input("Digite o preço:"))
    quantidade1 = int(input("Digite a quantidade:"))
    produto1 = Produto(nome1, preco1, quantidade1)

    nome2 = input("Digite o nome:")
    preco2 = float(input("Digite o preço:"))
    quantidade2 = int(input("Digite a quantidade:"))
    produto2 = Produto(nome2, preco2, quantidade2)

    nome3 = input("Digite o nome:")
    preco3 = float(input("Digite o preço:"))
    quantidade3 = int(input("Digite a quantidade:"))
    produto3 = Produto(nome3, preco3, quantidade3)

    while True:
      print("1 - Exibir produtos")
      print("2 - Realizar venda")
      print("3 - Repor estoque")
      print("4 - Mostrar valor em estoque")
      print("5 - Sair")
      opcao = int(input("Digite a sua opção:"))

      if opcao == 1:
        print("Primeiro produto")
        produto1.exibir()
        print("Segundo produto")
        produto2.exibir()
        print("Terceiro produto")
        produto3.exibir()

      elif opcao == 2:
          print("Escolha o produto:")
          print("1 - ", produto1.nome)
          print("2 - ", produto2.nome)
          print("3 - ", produto3.nome)

          produto = int(input("Digite o nome do produto:"))
          quantidade = int(input("Digite a quantidade de produto:"))

          if produto == 1:
              produto1.vender(quantidade)

          elif produto == 2:
              produto2.vender(quantidade)

          elif produto == 3:
              produto3.vender(quantidade)

          else:
              print("Produto não encontrado")

      elif opcao == 3:
          print("Repor o produto:")
          print("1 - ", produto1.nome)
          print("2 - ", produto2.nome)
          print("3 - ", produto3.nome)
          
          produto = int(input("Digite o número do produto"))
          quantidade = int(input("Digite a quantidade de produto:"))
          
          if produto == 1:
              produto1.adicionar(quantidade)
          
          elif produto == 2:
              produto2.adicionar(quantidade)
          
          elif produto == 3:
              produto3.adicionar(quantidade)
          
          else:
              print("Produto não encontrado")

      elif opcao == 4:
          print("Valor primeiro produto:", produto1.valor_estoque() )
          print("Valor segundo produto:", produto2.valor_estoque() )
          print("Valor terceiro produto:", produto3.valor_estoque() )

      elif opcao == 5:
          print("Encerrando...")
          break

      else:
          print("Opção inválida!")

main()

