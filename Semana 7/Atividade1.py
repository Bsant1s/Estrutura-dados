class No:
    def __init__(self, nome, gols):
        self.nome = nome
        self.gols = gols
        self.proximo = None


class Listaencadeada:
    def __init__(self):
        self.inicio = None

    def adicionar_inicio(self, nome, gols):
      no = No(nome, gols)

      no.proximo = self.inicio
      self.inicio = no

    def adicionar_final (self,nome, gols):
        no = No(nome, gols)
        if self.inicio == None:
            self.inicio = no
            return
        aux = self.inicio
        while aux.proximo != None:
            aux = aux.proximo
        aux.proximo = no

    def percorrer (self):
      aux = self.inicio

      while aux != None:
            print(aux.nome, "-", aux.gols, "gols") 
            aux = aux.proximo

    def media (self):
        aux = self.inicio
        total = 0
        quantidade = 0

        while aux != None:
            total = total + aux.gols
            quantidade += 1
            aux = aux.proximo

            if quantidade == 0:
                return 0

            return total / quantidade
    
def main():
    lista = Listaencadeada()
    lista.adicionar_inicio ("Casemiro", 1)
    lista.adicionar_inicio ("Pelé", 6)
    lista.adicionar_inicio ("Endrick", 4)
    
    lista.adicionar_final ("Cebolinha", 5)
    lista.adicionar_final ("Kannemall", 3)
    lista.adicionar_final ("Rodrygo", 1)

    print("Jogadores cadastrados:")
    lista.percorrer()
    print()
    print("Média dos gols:", lista.media())
main()
