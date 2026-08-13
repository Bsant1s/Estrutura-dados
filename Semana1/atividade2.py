
class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome 
        self.telefone = telefone
        self.email = email

agenda = []

for i in range(3):
  nome = input("Digite o nome:")
  telefone = input("Digite o telefone:")
  email = input("Digite o email:")

  contato = Contato (nome, telefone, email)
  agenda.append (contato)

for contato in agenda:
   print("Nome:", contato.nome)
   print("Telefone:", contato.telefone)
   print("Email:", contato.email)
         
        
