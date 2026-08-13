class Produto:
    def __init__(self, nome,preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def atualizar_estoque(self, valor):
        self.quantidade = self.quantidade + valor

nome = input("Digite o nome do primeiro preoduto:")
preco = float(input("Digite o preço:"))
quantidade = int(input("Digite a quantidade de produto:"))

produto1 = Produto(nome, preco, quantidade)

nome = input ("Digite o nome do segundo produto:")
preco = float(input("Digite o preço:"))
quantidade = int(input("Digite a quantidade de produto:"))

produto2 = Produto(nome, preco, quantidade)

valor = int(input("Quanto deseja adicionar ao estoque do primeiro produto:"))
produto1.atualizar_estoque(valor)

valor = int(input("Quanto deseja adicionar ao estoque do segundo produto:"))
produto2.atualizar_estoque(valor)

print("Produto:", produto1.nome)
print("Preço:", produto1.preco)
print("Quantidade:", produto1.quantidade)

print("Produto:", produto2.nome)
print("Preço:", produto2.preco)
print("Quantidade:", produto2.quantidade)
