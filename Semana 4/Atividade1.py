class No:
    def __init__(self, matricula, nome, notafinal):
        self.matricula = matricula
        self.nome = nome
        self.situacao = True
        self.notafinal = notafinal
        self.proximo = None

def inserir(lista, matricula, nome, notafinal):
    novo = No(matricula, nome, notafinal)

    if lista is None:
        return novo
    atual = lista

    while atual.proximo is not None:
        atual = atual.proximo

    atual.proximo = novo
    return lista

def listar(lista):
    if lista is None:
        print("Lista vazia")
        return 
    atual = lista 

    while atual is not None:
        print("Matrícula:", atual.matricula)
        print("Nome:", atual.nome)
        print("Situação:", atual.situacao)
        print("Nota:",atual.notafinal)

        atual = atual.proximo

def listar_ativos(lista):
    atual = lista

    while atual is not None:
        if atual.situacao == True:
            print(atual.matricula)
            print(atual.nome)
            print(atual.notafinal)

    atual = atual.proximo

def listar_desativados(lista):
    atual = lista

    while atual is not None:
        if atual.situacao == False:
            print(atual.matricula)
            print(atual.nome)
            print(atual.notafinal)

        atual = atual.proximo

def buscar (lista, matricula):
    atual = lista

    while atual is not None:
        if matricula == atual.matricula:
            return atual

        atual = atual.proximo
    return None

def alterar_nota(lista, matricula, nova_nota):
    aluno = buscar(lista, matricula)

    if aluno is not None:
        aluno.notafinal = nova_nota
        print("Nota atualizada")

    else:
        print("Aluno não encontrado")

def alterar_situacao(lista, matricula):
    aluno = buscar(lista, matricula)

    if aluno is not None:
        aluno.situacao = not aluno.situacao
        print("Nova situação:", aluno.situacao)
    else:
        print("Aluno não encontrado")

def remover (lista, matricula):
    if lista is None:
        return None

    if lista.matricula == matricula:
        return lista.proximo

    anterior = lista
    atual = lista.proximo

    while atual is not None:
        if atual.matricula == matricula:
            anterior.proximo = atual.proximo
            print("Aluno removido")
            return lista

        anterior = atual
        atual = atual.proximo
    print("Aluno não encontrado")
    return lista

def quantidade(lista):
    contador = 0
    atual = lista

    while atual is not None:
        contador += 1
        atual = atual.proximo

    return contador

def media_turma(lista):
    soma = 0
    contador = 0

    atual = lista
    while atual is not None:
        soma += atual.notafinal
        contador += 1
        atual = atual.proximo

    if contador == 0:
        return 0

    return soma / contador

def media_ativos(lista):
    soma = 0
    contador = 0

    atual = lista
    while atual is not None:
        if atual.situacao == True:
           soma += atual.notafinal
           contador += 1

        atual = atual.proximo

    if contador == 0:
        return 0
    return soma / contador

def menu():
    print("1 - Cadastrar aluno")
    print("2 - Listar todos")
    print("3 - Listar ativos")
    print("4 - Listar desativados")
    print("5 - Buscar aluno")
    print("6 - ALterar nota")
    print("7 - Alterar situação do aluno")
    print("8 - Remover aluno")
    print("9 - Quantidade de alunos cadastrados")
    print("10 - Média da turma")
    print("11 - Média de alunos ativos")
    print("12 - Sair")
    opcao = int(input("Digite sua opção:"))
    return opcao

def main():
    lista = None

    while True:
        opcao = menu()
        if opcao == 1:
            matricula = int(input("Digite a matrícula:"))
            nome = input("Digite o nome:")
            nota = float(input("Digite a nota:"))
            lista = inserir(lista, matricula, nome, nota)

        elif opcao == 2:
            listar(lista)

        elif opcao == 3:
            listar_ativos(lista)

        elif opcao == 4:
            listar_desativados(lista)

        elif opcao == 5:
            matricula = int(input("Matricula:"))
            aluno = buscar(lista, matricula)

            if aluno is not None:
                print("Matrícula:", aluno.matricula)
                print("Nome:", aluno.nome)
                print("Situação:", aluno.situacao)
                print("Nota:", aluno.notafinal)

            else:
                print("Aluno não encontrado")

        elif opcao == 6:
            matricula = int(input("Matricula:"))
            nota = float(input("Nova nota:"))

            alterar_nota(lista, matricula, nota)

        elif opcao == 7:
            matricula = int(input("Matricula:"))

            alterar_situacao(lista, matricula)

        elif opcao == 8:
            matricula = int(input("Matricula:"))

            lista = remover(lista, matricula)

        elif opcao == 9:
            print("Quantidade de alunos:", quantidade(lista))

        elif opcao == 10:
            print("Média da turma:", media_turma(lista))

        elif opcao == 11:
            print("Média dos alunos atuvos:", media_ativos(lista))

        elif opcao == 12:
            print("Encerrando...")
            break

        else:
            print("Erro, tente novamente")

main()
