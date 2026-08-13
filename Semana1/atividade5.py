class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def calcular_bonus(self):
        if self.cargo == "Gerente":
            bonus = self.salario * 0.10
        else:
            bonus = self.salario * 0.05

        return bonus

nome = input("Digite o nome:")
salario = float (input("Digite o salário:"))
cargo = input("Digite o cargo:")

funcionario1 = Funcionario(nome, salario, cargo)

nome = input("Digite o nome:")
salario = float(input("Digite o salário:"))
cargo = input("Digite o cargo:")

funcionario2 = Funcionario (nome, salario, cargo)

bonus1 = funcionario1.calcular_bonus()
bonus2 = funcionario2.calcular_bonus()

print("Nome:", funcionario1.nome)
print("Salário com bônus:", funcionario1.salario + bonus1)

print("Nome:", funcionario2.nome)
print("Salário com bônus:", funcionario2.salario + bonus2)
