class Livro:
    def __init__(self, titulo, autor, numero_p):
        self.titulo = titulo
        self.autor = autor
        self.numero_p = numero_p

    def verificar_tamanho(self):
        if self.numero_p <= 100:
            print("O livro é curto")
        else:
            print("O livro é longo")

titulo = input ("Digite o título do primeiro livro:")
autor = input ("Digite o autor:")
numero_p = int(input("Digite o número de páginas:"))

livro1 = Livro(titulo, autor, numero_p)

titulo = input ("Digite o título do segundo livro:")
autor = input ("Digite o autor:")
numero_p = int(input("Digite o número de páginas:"))

livro2 = Livro(titulo, autor, numero_p)

print("Título:", livro1.titulo)
print("Autor:", livro1.autor)
livro1.verificar_tamanho()

print("Título:", livro2.titulo)
print("Autor:", livro2.autor)
livro2.verificar_tamanho()
