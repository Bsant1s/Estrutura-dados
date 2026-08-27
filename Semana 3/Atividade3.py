class No:
    def __init__(self, id, nome, artista, duracao):
        self.id = id
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        self.proximo = None
        self.anterior = None


def inserir(lista, id, nome, artista, duracao):
    novo = No(id, nome, artista, duracao)

    if lista is None:
        return novo

    atual = lista

    while atual.proximo is not None:
        atual = atual.proximo

    atual.proximo = novo
    novo.anterior = atual

    return lista

def listar(lista):
    if lista is None:
        print("Playlist vazia")
        return

    atual = lista

    while atual is not None:
        print("ID:", atual.id)
        print("Nome:", atual.nome)
        print("Artista:", atual.artista)
        print("Duração:", atual.duracao)

        atual = atual.proximo

def remover(lista, id):
    if lista is None:
        print("Playlist vazia")
        return lista

    atual = lista

    while atual is not None:

        if atual.id == id:

            if atual.anterior is None:
                lista = atual.proximo

                if lista is not None:
                    lista.anterior = None

            else:
                atual.anterior.proximo = atual.proximo

                if atual.proximo is not None:
                    atual.proximo.anterior = atual.anterior

            print("Música removida")
            return lista

        atual = atual.proximo

def buscar_nome(lista, nome):
    atual = lista

    while atual is not None:

        if atual.nome == nome:
            print("Música encontrada")
            print("ID:", atual.id)
            print("Nome:", atual.nome)
            print("Artista:", atual.artista)
            print("Duração:", atual.duracao,)
            return

        atual = atual.proximo

    print("Música não encontrada")

def buscar_artista(lista, artista):
    atual = lista

    while atual is not None:

        if atual.artista == artista:
            print("Música encontrada")
            print("ID:", atual.id)
            print("Nome:", atual.nome)
            print("Artista:", atual.artista)
            print("Duração:", atual.duracao)
            return

        atual = atual.proximo

    print("Música não encontrada")

def duracao_total(lista):
    total = 0
    atual = lista

    while atual is not None:
        total += atual.duracao
        atual = atual.proximo

    print("Duração total:", total)

def avancar(atual):
    if atual is None:
        print("Playlist vazia")
        return atual

    if atual.proximo is not None:
        atual = atual.proximo
        print("Próxima música:", atual.nome)
    else:
        print("Você já está na última música")

    return atual

def voltar(atual):
    if atual is None:
        print("Playlist vazia")
        return atual

    if atual.anterior is not None:
        atual = atual.anterior
        print("Música anterior:", atual.nome)
    else:
        print("Você já está na primeira música")

    return atual

def main():

    lista = None
    atual = None

    while True:
        print("1 - Adicionar música")
        print("2 - Listar todas as músicas")
        print("3 - Remover música")
        print("4 - Buscar música")
        print("5 - Mostrar duração total")
        print("6 - Avançar / Voltar")
        print("7 - Sair")
        opcao = int(input("Digite a sua opção: "))

        if opcao == 1:

            id = int(input("Digite o ID da música: "))
            nome = input("Digite o nome da música: ")
            artista = input("Digite o artista: ")
            duracao = float(input("Digite a duração em minutos: "))

            lista = inserir(lista, id, nome, artista, duracao)

            if atual is None:
                atual = lista

            print("Música adicionada")

        elif opcao == 2:
            listar(lista)

        elif opcao == 3:

            id = int(input("Digite o ID da música que deseja remover: "))

            if atual is not None and atual.id == id:
                if atual.proximo is not None:
                    atual = atual.proximo
                elif atual.anterior is not None:
                    atual = atual.anterior
                else:
                    atual = None

            lista = remover(lista, id)

        elif opcao == 4:
            print("1 - Buscar por nome")
            print("2 - Buscar por artista")
            busca = int(input("Digite a sua opção: "))

            if busca == 1:

                nome = input("Digite o nome da música: ")
                buscar_nome(lista, nome)

            elif busca == 2:

                artista = input("Digite o nome do artista: ")
                buscar_artista(lista, artista)

            else:
                print("Erro, tente novamente")

        elif opcao == 5:
            duracao_total(lista)

        elif opcao == 6:
            print("1 - Avançar para próxima música")
            print("2 - Voltar para música anterior")
            movimento = int(input("Digite a sua opção: "))

            if movimento == 1:
                atual = avancar(atual)

            elif movimento == 2:
                atual = voltar(atual)

            else:
                print("Erro, tente novamente")

        elif opcao == 7:

            print("Encerrando...")
            break

        else:
            print("Erro, tente novamente")


main()
