def dia_siguiente(dia, mes, anio):
    """
    contrato: Calcula cual es la fecha siguiente a la ingresada.
    pre: Recibe 3 enteros positivos que simbolizan una fecha.
    post: Retorna una tupla.
    """
    if mes == 2 :
        if anio % 400 == 0  or anio % 4 == 0 and anio % 100 != 0 :
            dias = 29 

        else:
            dias = 28 
    elif mes in  (4,6,9,11):
        dias = 30

    else:
        dias = 31

    if dia == dias : #si no es el ultimo dia 
        if mes == 12:
            dia = 1
            mes = 1
            anio += 1 
        else:
            dia = 1 
            mes += 1

    else : 
        dia += 1 

    return  dia, mes, anio


dia = int(input("Ingrese un dia: "))

mes = int(input("Ingrese un mes: "))

anio = int(input("ingrese un año: "))

num_dias = int(input("ingrese los dias a sumar: "))

for i in range (num_dias):
    dia, mes, anio = dia_siguiente(dia, mes, anio) 

print(f"La fecha despues de {num_dias} dias es : {dia, mes, anio}")

dia_2 =int(input("Ingrese un segundo dia: "))

mes_2=int(input("Ingrese un segundo mes: "))

anio_2 =int(input("ingrese un segundo año: "))

dif_dia = 0 

while (anio_2, mes_2 , dia_2) != (anio, mes, dia):
    if (anio_2, mes_2 , dia_2) < (anio, mes, dia):
        dia_2, mes_2 , anio_2 = dia_siguiente (dia_2, mes_2 , anio_2)
    else:
        dia, mes, anio = dia_siguiente(dia, mes, anio)
    dif_dia += 1

print(f"La diferencia de dias entre {dia_2, mes_2, anio_2} y {dia, mes, anio} es de : {dif_dia}")


            






