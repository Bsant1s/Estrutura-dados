class Pilha:
    def __init__(self):
        self.elementos = []

    def empilhar(self, dado):
        self.elementos.append(dado)

    def desempilhar(self):
        if len(self.elementos) > 0:
            return self.elementos.pop()
        else:
            print("A pilha está vazia.")

    def percorrer(self):
        for elemento in self.elementos:
            print(elemento)

    def topo(self):
        if len(self.elementos) > 0:
            return self.elementos[-1]
        else:
            print("A pilha está vazia.")

    def esta_vazia(self):
        return len(self.elementos) == 0


pilha = Pilha()

pilha.empilhar(10)
pilha.empilhar(20)
pilha.empilhar(30)

print("Topo da pilha:", pilha.topo())

pilha.desempilhar()

print("Topo da lista:", pilha.topo())

print("A pilha está vazia:", pilha.esta_vazia())
