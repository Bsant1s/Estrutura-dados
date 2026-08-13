class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        media = (self.notas[0] + self.notas[1] + self.notas[2]) / 3
        return media

turma = []

for i in range(3):
    nome = input("Digite o nome do aluno:")

    nota1 = float(input("Digite a primeira nota:"))
    nota2 = float(input("Digite a segunda nota:"))
    nota3 = float(input("Digite a terceira nota:"))

    notas = [nota1, nota2, nota3]

    aluno = Aluno(nome, notas)
    turma.append(aluno)

for aluno in turma:
    print("Nome:", aluno.nome)
    print("Média:", aluno.calcular_media())
