
#LIBRERIA
import random as rn

def generar_lista(num: int)-> list[int]:
    """
        contrato
        Carga una lista con números al azar
        pre:Recibe enteros positivo
        post: Retorna una lista con  elementos entre  1 y 100 
        """

    lista =  []

    for i in range (num):
        lista.append(rn.randint(1,100))

    return lista


def elemento_repetido(lista:list[int])-> bool:

    for e in lista:
        if lista.count(e) >= 1 :
            return True
    return False


def nueva_lista(lista:list[int])-> list:
    lista2 = []
    for e in lista:
        if lista.count(e)  == 1  :
            lista2.append(e)

    return lista2
    
def main():

    n =int(input("Ingrese la cantidad de los números aleatorios"))
    lista_1 = generar_lista(n) 

    print (lista_1)

    print(elemento_repetido(lista_1))

    lista_2 = nueva_lista(lista_1)

    print(lista_2)


main()











