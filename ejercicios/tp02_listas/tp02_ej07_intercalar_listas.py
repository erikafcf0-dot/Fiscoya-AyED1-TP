def intercalar(lista1 : list[int], lista2: list[int])->None:
    """
    Intercala los elementos de lista2 entre los elementos de lista1.
    pre: Recibe de dos listas de números enteros.
    post:Modifica lista1 intercalando los elementos de lista2, 
    sin crear una nueva lista.
    """
    for i, e in enumerate(lista2):
        pos = i*2 + 1
        lista1[pos:pos] = [e]

def main()->None:
    """
    Ejecuta el programa principal para verificar la intercalación
    de dos listas.
    pre:No recibe parámetros.
    post:Crea dos listas, muestra sus valores originales, intercala
    los elementos de lista2 en lista1 y muestra lista1 modificada
    """
    lista1 = [8,1,3]
    lista2 = [5,9,7]

    print("Lista original:")
    print(lista1)

    print("lista 2:")
    print(lista2)

    intercalar(lista1, lista2)

    print("Lista intercalada:")
    print(lista1)

main()

