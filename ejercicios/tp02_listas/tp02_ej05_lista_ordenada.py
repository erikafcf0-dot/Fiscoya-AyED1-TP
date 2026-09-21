def lista_ordenada(lista: list)-> bool:
    """
    contrato
    pre:
    post:
    """
    for i in range(len(lista)-1):
        if lista[i]> lista [i + 1]:
            return False
    return True


def main()->None:
    lista1 = [1,2,3]
    lista2 = ["b","a"]
    lista3 = [11,14,16]
    lista4 = ["a","b"]

    print(lista1)
    print(lista_ordenada(lista1))

    print(lista2)
    print(lista_ordenada(lista2))

    print(lista3)
    print(lista_ordenada(lista3))

    print(lista4)
    print(lista_ordenada(lista4))

main()