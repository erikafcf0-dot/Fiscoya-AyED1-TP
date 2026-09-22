def vericar_oblongo(num: int) -> bool:
    """
    Contrato:
    Determina si un número es oblongo.
    Pre: Recibe un entero positivo.
    Post: Retorna un booleano.

    """
    
    for i in range(num+1):
        if i *(i+1) == num:
            return True
        elif i *(i+1) > num:
            return False 

num = int(input("Ingrese el numero a verificar: " ))

print(vericar_oblongo(num))



def triangular(num: int)-> bool:
    """
    Contrato:
    Determina si un número es oblongo.
    Pre: Recibe un entero positivo.
    post: Retorna un booleano.
    """

    num_t= 0
    for i in range(num):
        num_t += i
        if num_t == num :
            return True
        elif num_t > num:
            return False


num = int(input("Ingrese el numero a verificar: " ))

print(triangular(num))

        
