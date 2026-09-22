def lista_ordenada(lista: list)-> bool:
    """
    Verifica si una lista está 
    ordenada de forma ascendente
    pre:Recibe una lista con elementos que se puedan comparar entre sí.
    post:Retorna True si todos los elementos de la lista están ordenados de forma
    ascendente o False en caso contrario. 
    """
    for i in range(len(lista)-1):
        if lista[i]> lista [i + 1]:
            return False
    return True


def main()->None:
    """
    Ejecuta  el funcionamiento de la función lista_ordenada. 
    pre: No recibe parámetros
    post: Muestra distintas listas ordenadas de forma ascendente
    """


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