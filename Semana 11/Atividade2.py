def mostrar_valor (n):
    if n < 0:
        return 0
    print(n)
    mostrar_valor(n - 2)

mostrar_valor (20)
    
