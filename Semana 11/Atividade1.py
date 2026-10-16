def mostrar_valor (n):
    if n < 1:
       return 
    print (n)
    mostrar_valor (n - 1)

mostrar_valor (10)
