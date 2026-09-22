def normalizar(lista:list[int])->list[float]:
    """
    Normaliza los valores de una lista
    pre:Recibe una lista de números enteros de la cual la suma es distinta a 0
    post:Retorna una lista con los valores normalizados.
    """
    suma = sum(lista) 

    return [e / suma for e in lista]

def main()->None:
    """
    Ejecuta la función normalizar.
    pre:No recibe parámetros.
    post: Muestra las dos listas originales y sus listas normalizadas. 
    """

    lista1= [1,1,2]
    print("La lista original es : ")
    print(lista1)

    print("lista normalizada es :")
    print(normalizar(lista1))

    lista2 = [2,3,5]
    print("La lista original es : ")

    print(lista2)
    print("La lista normalizada es :")
    print(normalizar(lista2))


main()