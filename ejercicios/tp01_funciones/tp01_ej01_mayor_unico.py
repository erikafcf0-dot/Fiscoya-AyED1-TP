def mayor_unico(num1: int,num2: int,num3: int) -> int:
    """
    Contrato : Compara tres números enteros positivos  y determina si existe un unico mayor.
    pre: recibe 3 números positivos
    post: Devuelve el entero con mayor valor o un -1 cuando no exista un solo mayor.

    """
    if num1 > num2:
        if num1> num3:
            return num1

        elif num1 < num3:
            return num3

        else:
            return -1

    elif num1 < num2:
        if num2 > num3:
            return num2
        elif num2 < num3:
            return num3
        else:
            return -1

    elif num1 == num2:
        if num1 > num3:
            return -1
        elif num3 > num1:
            return num3
        else :
            return -1


def main():
    """
    Contrato:
    Ejecuta el código principal.
    Pre: No recibe nada.
    Post: No retorna nada, solo ejecuta la función y pide los números al usuario.
    """

    num1= 0
    while num1 <= 0 :
        num1 = int(input("ingrese el numero a comparar: "))   

    num2= 0
    while num2 <= 0 :
        num2 = int(input("ingrese el numero a comparar: "))        

    num3= 0
    while num3 <= 0 :
        num3 = int(input("ingrese el numero a comparar: "))


    print(mayor_unico(num1,num2,num3))

main()