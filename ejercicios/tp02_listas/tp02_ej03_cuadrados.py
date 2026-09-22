

def cargar_cuadrados(n: int)-> list[int]:
    """
    Genera una lista con los cuadrados entre 1 y otro número. 
    pre:Recibe un número entero positivo.
    post:Retorna una lista con los cuadrados de  los números.
    """


    return [num ** 2  for num  in range(1, n + 1)]


nume= int(input("Ingrese un número para definir el largo: "))

lista = cargar_cuadrados(nume) 

print(lista)

print(lista[-10:])
