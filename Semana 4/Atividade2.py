class No:
    def __init__(self, codigo, nome, idade, prioridade):
        self.codigo = codigo
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade
        self.proximo = None
        self.anterior = None

def prioridade():
    print("1 - Emergêcia")
    print("2 - Muita emergência") 
    print("3 - Urgente")
    print("4 - Pouco urgente")
    print("5 - Não urgente")  
    opcao = int(input("Digite a sua opção:"))

    if opcao == 1:
        return "Emergência"
    elif opcao == 2:
        return "Muita emergencia"
    elif opcao == 3:
        return "Urgente"
    elif opcao == 4:
        return "Pouco urgente"
    elif opcao == 5:
        return "Não urgente"
    else:
        return None

def inserir (lista, codigo, nome, idade, prioridade):
    novo = No (codigo, nome, idade, prioridade)

    if lista is None:
        return novo

    atual = lista
    while atual.proximo is not None:
        atual = atual.proximo

    atual.proximo = novo
    novo.anterior = atual
    return lista

def listar (lista):
    if lista is None:
        print("Nenhum paciente na fila")
        return 
    atual = lista
    while atual is not None:
        print("Código:", atual.codigo)
        print("Nome:", atual.nome)
        print("Idade:", atual.idade)
        print("Prioridades:", atual.prioridade)
        atual = atual.proximo

def inverso(lista):
    if lista is None:
        print("Nenhum paciente nas fila")
        return 
    atual = lista
    while atual.proximo is not None:
        atual = atual.proximo
    while atual is not None:
        print("Código:", atual.codigo)
        print("Nome:", atual.nome)
        print("idade:", atual.idade)
        print("Prioridades:", atual.prioridade)
        atual = atual.anterior

def buscar(lista, codigo):
    atual = lista

    while atual is not None:
        if atual.codigo == codigo:
            return atual
        atual= atual.proximo
    return None

def remover(lista, codigo):
    atual = buscar(lista, codigo)

    if atual is None:
      print ("Nenhum paciente na fila")
      return lista

    if atual.anterior is None:
        lista = atual.proximo

        if lista is not None:
            lista.anterior = None
    else:
        atual.anterior.proximo = atual.proximo
        if atual.proximo is not None:
            atual.proximo.anterior = atual.anterior

        print("Paciente removido")
        return lista

def atender_urgente(lista):
    if lista is None:
        print("Nenhum paciente na lista")
        return lista

    atual = lista
    paciente = lista

    while atual is not None:

        if atual.prioridade == "Emergência":
            paciente = atual
            break

        elif atual.prioridade == "Muito urgente":
            if paciente.prioridade != "Emergência":
                paciente = atual

        elif atual.prioridade == "Urgente":
            if paciente.prioridade != "Emergência" and paciente.prioridade != "Muito urgente":
                paciente = atual

        elif atual.prioridade == "Pouco urgente":
            if paciente.prioridade == "Não urgente":
                paciente = atual

        atual = atual.proximo

    print("Paciente atendido:")
    print("Código:", paciente.codigo)
    print("Nome:", paciente.nome)
    print("Idade:", paciente.idade)
    print("Prioridade:", paciente.prioridade)

    return remover(lista, paciente.codigo)

def listar_prioridade (lista, prioridade):
    if lista is None:
        print("Nenhum paciente na lista")
        return 
    atual = lista
    encontrou = False

    while atual is not None:
        if atual.prioridade == prioridade:
            print("Código:", atual.codigo)
            print("Nome:", atual.nome)
            print("Idade:", atual.idade)
            print("Prioridade:", atual.prioridade)
            encontrou = True
        atual = atual.proximo

    if not encontrou:
        print("Nenhum paciente com essa prioridade")

def quantidade (lista):
    contador = 0
    atual = lista

    while atual is not None:
        contador += 1
        atual = atual.proximo

    return contador

def menu():
    print("1 - Cadastrar paciente")
    print("2 - Remover paciente")
    print("3 - Localizar paciente")
    print("4 - Atender peciente mais urgente")
    print("5 - Lista do primeiro para o último")
    print("6 - Listar por prioridade")
    print("7 - LIstar do último para o primeiro")
    print("8 - Quantidade de pacientes")
    print("9 - Sair")
    opcao = int(input("Digite sua opção:"))
    return opcao

def main():
    lista = None

    while True:
        opcao = menu()

        if opcao == 1:
            codigo = int(input("Código:"))
            nome = input("Digite o nome:")
            idade = int(input("Digite a idade:"))
            opcao_prioridade = prioridade()

            if opcao_prioridade is None:
                print("Erro, tente novamente")
            else:
                lista = inserir(lista, codigo, nome, idade, opcao_prioridade)
                print("Paciente cadastrado")

        elif opcao == 2:
            codigo = int(input("Digite o código do paciente"))
            lista = remover(lista, codigo)

        elif opcao == 3:
            codigo = int(input("Digite o código do paciente:"))
            paciente = buscar(lista, codigo)

            if paciente is None:
                print("Paciente não encontrado")
            else:
                print("Código:", paciente.codigo)
                print("Nome:", paciente.nome)
                print("Idade:", paciente.idade)
                print("Prioridade:", paciente.prioridade)

        elif opcao == 4:
            lista = atender_urgente(lista)

        elif opcao == 5:
            listar(lista)

        elif opcao == 6:
            opcao_prioridade = prioridade()

            if opcao_prioridade is None:
                print("Erro, tente novamente")
            else:
                listar_prioridade(lista, opcao_prioridade)

        elif opcao == 7:
            inverso(lista)

        elif opcao == 8:
            total = quantidade(lista)
            print("Quantidade de pacientes aguardando:", total)

        elif opcao == 9:
            print("Encerrando...")
            break

        else:
            print("Erro, tente novamente")

main()
