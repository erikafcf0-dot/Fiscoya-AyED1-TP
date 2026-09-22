def cargar_matriz(num:int)-> list [list[int]]:

    """

    """
    matriz = []
    for i in range(num):

        fila=[]

        for j in range(num):
            numero = int(input(f"Ingrese un número entero: "))

            fila.append(numero)


        matriz.append(fila)

    return matriz 

def mostrar(matriz:list[list[int]])->None:
    """
    """
    for fila in matriz:
        print(fila)

def ordenar(matriz:list[list[int]])->None:
    """
    """
    for fila in matriz:
        fila.sort()



def intercambiar_filas(matriz: list[list[int]], fila: int, fila1: int) -> None:
    """
    """
    matriz[fila-1], matriz[fila1-1] = matriz[fila1-1], matriz[fila-1]

def intercambiar_columnas (matriz:list[list[int]],columna1:int,columna2:int)-> None:
    """
    """
    for i in range(len(matriz)):

        aux = matriz[i][columna1]
        matriz[i][columna1] = matriz[i][columna2]
        matriz[i][columna2] = aux

def transponer(matriz: list[list[int]])->None:
    """
    """
    for i in range(len(matriz)):
        for j in range(i +1,len(matriz)):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux


def promedio_fila(matriz:list[list[int]],fila:int)-> float:
    suma = 0 
    for e in matriz [fila]:
        suma += e
    promedio = suma /len(matriz[fila])

    return promedio


def porcentaje_impares(matriz: list [list[int]], columna : int)->float:

    cant_impares = 0 
    for i in range(len(matriz)):
        if matriz [i][columna] % 2 != 0 :
            cant_impares += 1

    porcentaje = cant_impares * 100 / len(matriz)

    return  porcentaje

def simetrica_principal(matriz: list[list[int]])->bool:
    """
    """

    for i in range(len(matriz)):
        for j in range(len(matriz)):

            if matriz[i][j] != matriz[j][i]:
                return False

    return True

def simetrica_secundaria(matriz:list[list[int]])-> bool:
    """

    """
    num = len(matriz)

    for i in range(num):

        for j in range(num):

            if matriz[i][j] != matriz[num -1 - j][ num - 1 - i ]:
                return False


    return True

def col_palindromos(matriz:list[list[int]])->list[int]:
    """
    """
    palindromo  = []
    

    for j in range(len(matriz)):

        columna =[]

        for i in range (len(matriz)):

            columna.append(matriz[i][j])

        if columna == columna[::-1]:
            palindromo.append(j + 1)

    return palindromo


def main() -> None:
    """
    Contrato:
    Ejecuta y verifica todas las funciones realizadas sobre la matriz.

    Pre:
    No recibe parámetros.

    Post:
    Carga una matriz de N x N y ejecuta todas las operaciones solicitadas,
    mostrando los resultados de cada una.
    """

    num = int(input("Ingrese el tamaño de la matriz: "))

    while num <= 0:
        num = int(input("Error. Ingrese un número mayor que 0: "))


    # A - CARGAR MATRIZ

    matriz = cargar_matriz(num)

    print("\nMatriz original:")
    mostrar(matriz)


    # B - ORDENAR FILAS

    ordenar(matriz)

    print("\nMatriz con las filas ordenadas:")
    mostrar(matriz)


    # C - INTERCAMBIAR FILAS

    fila = int(input("\nIngrese la primera fila a intercambiar: "))
    fila1 = int(input("Ingrese la segunda fila a intercambiar: "))

    intercambiar_filas(matriz, fila, fila1)

    print("\nMatriz después de intercambiar las filas:")
    mostrar(matriz)


    # D - INTERCAMBIAR COLUMNAS

    columna1 = int(input("\nIngrese la primera columna a intercambiar: "))
    columna2 = int(input("Ingrese la segunda columna a intercambiar: "))

    intercambiar_columnas(matriz, columna1 - 1, columna2 - 1)

    print("\nMatriz después de intercambiar las columnas:")
    mostrar(matriz)


    # E - TRANSPONER MATRIZ

    transponer(matriz)

    print("\nMatriz transpuesta:")
    mostrar(matriz)


    # F - PROMEDIO DE UNA FILA

    fila = int(input("\nIngrese una fila para calcular el promedio: "))

    promedio = promedio_fila(matriz, fila - 1)

    print(f"El promedio de la fila {fila} es: {promedio}")


    # G - PORCENTAJE DE IMPARES DE UNA COLUMNA

    columna = int(input("\nIngrese una columna: "))

    porcentaje = porcentaje_impares(matriz, columna - 1)

    print(f"El porcentaje de elementos impares es: {porcentaje}%")


    # H - SIMETRÍA DIAGONAL PRINCIPAL

    print("\n¿La matriz es simétrica respecto de la diagonal principal?")

    print(simetrica_principal(matriz))


    # I - SIMETRÍA DIAGONAL SECUNDARIA

    print("\n¿La matriz es simétrica respecto de la diagonal secundaria?")

    print(simetrica_secundaria(matriz))


    # J - COLUMNAS PALÍNDROMAS

    print("\nColumnas palíndromas:")

    print(col_palindromos(matriz))


main()