#LIBRERIAS
import random as rn

#FUNCIONES
def num_al_azar()-> list[int]:
    """
    contrato
    Carga una lista con números al azar
    pre:no recibe nada
    post: Retorna una lista con indices aleatorios de 2 digitos y numeros aleatorios de 4 digitos.  
    """

    lista= []

    indice = rn.randint(10,99)
    for i in range(indice):
        lista.append(rn.randint(1000,9999))

    return lista


def calcular_prod(lista: list[int])-> int:
    """
    contrato
    Calcula el producto de los elementos de la lista anterior 
    pre: Recibe la lista anterior
    post: Devuelve el producto de los elementos de la lista.
    """
    producto = 1
    for e in lista:
        producto *= e 
    return producto


def eliminar_apariciones(lista: list[int], valor: int)-> list[int]:
    """
    contrato
    Eliminar todas las apariciones de un valor .
    pre: Recibe los valores de la lista anterior.
    post: Retorna la lista sin las apariciones.

    """
    return [e for e in lista if valor != e] 

def es_capicua(lista: list[int]) -> bool :
    """
    contrato
    Determina si una lista es capicúa
    pre: Recibe cualquier lista
    post: Retorna  booleano

    """   
    return lista == lista.reverse()  

def main():

    lista1 = num_al_azar()
    print(lista1)

    print(f"El producto de todos los elementos de la lista es {calcular_prod(lista1)}: ")

    aparicion = int(input("Ingrese el número que quiere eliminar:"))

    lista1 = eliminar_apariciones(lista1 , aparicion)
    print(lista1)

    print(es_capicua(lista1))

main()
