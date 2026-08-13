class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        media = (self.notas[0] + self.notas[1] + self.notas[2]) / 3
        return media

    def verificar_aprovado(self):
        media = self.calcular_media()
        if media >= 7:
            print("Aprovado")
        else: 
            print("Reprovado")

nome = input("Digite o nome do primeiro aluno:")
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))

notas = [nota1, nota2, nota3]

aluno1 = Aluno(nome, notas)

nome = input("Digite o nome do segundo aluno:")
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))

notas = [nota1, nota2, nota3]

aluno2 = Aluno(nome, notas)

print("Nome;", aluno1.nome)
print("Média:", aluno1.calcular_media())
print("Situação:", aluno1.verificar_aprovado())

print("Nome:", aluno2.nome)
print("Média:", aluno2.calcular_media())
print("Situação:", aluno2.verificar_aprovado())
