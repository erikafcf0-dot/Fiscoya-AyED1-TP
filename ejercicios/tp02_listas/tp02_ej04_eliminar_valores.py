def eliminar_elementos(lista : list[int], lista1 : list[int]) -> None:
    """
    Elimina de una lista los elementos de otra lista.
    pre:Recibe dos listas de números enteros.
    post:Modifica la primera lista eliminando los valores que se
    encuentren en la segunda lista.
    """
    for e in lista1:
        while e in lista:
            lista.remove(e)


lista1 = [12, 11,18,23,11,22,34,67]
lista2 =[67,22,12,11]

print(f"Lista original: {lista1}")
print(f"Elementos a  eliminar: {lista2}")

eliminar_elementos(lista1,lista2) 
print(lista1)
