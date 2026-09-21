

def cargar_cuadrados(n: int)-> list[int]:
    """
        contrato
       
        pre:
        post:  
        """


    return [num ** 2  for num  in range(1, n + 1)]


nume= int(input("Ingrese un número para definir el largo: "))

lista = cargar_cuadrados(nume) 

print(lista)

print(lista[-10:])
