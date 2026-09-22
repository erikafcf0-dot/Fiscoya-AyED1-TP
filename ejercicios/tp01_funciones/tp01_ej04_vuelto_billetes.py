def calcular_vuelto(recibido: int, total: int)-> None:
    """
    Contrato:
    Determina cuanto tiene que darse de cambio al cliente.
    pre: Recibe dos enteros positivos que indican el costo total y la cantidad con la que pago el cliente.
    post: No retorna nada, solo hace print por cada billete que se le entrega de vuelta.
    """
    vuelto = recibido - total

    if vuelto < 0 :
        print("No se puede abonar la compra por falta de efectivo ( es fin de mes :c)")
    elif vuelto == 0 :
        print("El cliente no recibe vuelto")

    else:
        if vuelto >= 5000 :
            b_cinco= vuelto // 5000
            vuelto %= 5000
            print(f" El vuelto en billetes de 5000 son : {b_cinco}")

        if vuelto >= 1000:
            b_mil= vuelto // 1000
            vuelto %= 1000
            print(f" El vuelto en billetes de 1000 son : {b_mil}")

        if vuelto >= 500 :
            b_quin= vuelto // 500
            vuelto %= 500
            print(f" El vuelto en billetes de 500 son : {b_quin}")
        
        
        if vuelto >= 200 :
            b_dosc= vuelto // 200
            vuelto %= 200
            print(f" El vuelto en billetes de 200 son : {b_dosc}")
        
        if vuelto >= 100 :
            b_cien= vuelto // 100
            vuelto %= 100
            print(f" El vuelto en billetes de 100 son : {b_cien}")
        
        if vuelto >= 50 :
            b_cincuenta= vuelto // 50
            vuelto %= 50
            print(f" El vuelto en billetes de 50 son : {b_cincuenta}")
        
        if vuelto >= 10 :
            b_diez= vuelto // 10
            vuelto %= 10
            print(f" El vuelto en billetes de 10 son : {b_diez}")


while True:
        
    total = int(input("ingrese el total de la compra: "))
    if total >= 10:
        break
    else:
        print("El total de la compra tiene que ser mayor  a 10  ")

while True :
    recibido =int(input("ingrese la cantidad recibida: "))
    if recibido  >= 10:
        break
    else:
        print("La cantidad recibida tiene que ser mayor a  10 ")


calcular_vuelto(recibido, total)


                                        
                                                        