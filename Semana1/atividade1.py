preco = float(input("Digite o preço:"))
quantidade = float(input("Digite a quantidade:"))

class Produto:
    def __init__(self, preco, quantidade):
        self.preco = preco
        self.quantidade = quantidade 
        self.total = 0

    def calcular_total(self ):
        return self.preco * self.quantidade

    def mostrar_total(self):
        print("Valor de produto em estoque:", self.calcular_total())

p = Produto (preco, quantidade)
p.mostrar_total()
