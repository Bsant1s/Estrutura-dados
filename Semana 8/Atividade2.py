class NoDuplo:
    def __init__(self, id, nome, status):
        self.id = id 
        self.nome = nome
        self.status = status 
        self.proximo = None
        self.anterior = None
        
def inserir (lista, id, nome, status):
    no = NoDuplo (id, nome, status)

    if lista is None:
        lista = no
        return lista

    aux = lista
    while aux.proximo is not None:
        aux = aux.proximo

    aux.proximo = no
    no.anterior = aux
    no.proximo = None
    return lista

def  listar_frente (lista):

    aux = lista
    while aux is not None:
        print (aux.id)
        print (aux.nome)
        print (aux.status)

        aux = aux.proximo

def listar_atras (lista):
    aux = lista
    while aux.proximo  is not None:
        aux = aux.proximo 

    while aux is not None:
        print (aux.id)
        print (aux.nome)
        print (aux.status)

        aux = aux.anterior

def remover (lista, id):

    if lista is None:
        print ("Lista vazia")
        return lista

    aux = lista
    if lista.id == id:
        lista = lista.proximo
        
        if lista is not None:
          lista.anterior = None
          return lista


    while aux.proximo is not None and aux.proximo.id != id:
        aux = aux.proximo

    if aux.proximo != None:
        aux.proximo = aux.proximo.proximo
        
        if aux.proximo is not None:
           aux.proximo.anterior = aux
    else:
        print("Elemento não encontrado")
    return lista

def ligar (lista, id):
    aux = lista

    while aux is not None:
      if aux.id == id:
        aux.status = True
        return lista

    aux = aux.proximo
    print("Servidor não encontrado")
    return lista

def desligar (lista, id):
    aux = lista

    while aux is not None:
      if aux.id == id:
        aux.status = False
        return lista

    aux = aux.proximo
    print("Servidor não encontrado")
    return lista

def main():

  lista = None
  lista = inserir(lista, 1, "Servidor web", True)
  lista = inserir(lista, 2, "Servidor hardware", False)

  print("Servidores:") 
  listar_frente (lista)

  lista = remover (lista, 1)

  ligar (lista, 2)
  listar_frente (lista)
  print()
  desligar (lista,2)
  listar_frente (lista)
  
main()
