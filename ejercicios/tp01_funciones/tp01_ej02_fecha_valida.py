def es_biciesto(ano: int) -> bool :
    """
    verifica si el año es biciesto
    pre: Recibe un año (entero positivo) 
    post: Indica si el año es biciesto mediante un booleano  
    
    """
    if ano % 4 == 0 and ano % 100 != 0:
        return True 
    elif ano % 400 == 0 :
        return True
    else:
        return False

def validar_dia(dia: int, mes: int, ano: int) -> bool:
    """
    Contrato:
    Valída si la fecha ingresada es válida o si no.
    Pre: Recibe tres enteros que representan una fecha.
    Post: Retorna un booleano en base a si la fecha es correcta.
    """
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia >= 1 and dia <= 31:
            return True
        else:
            return False

    elif mes ==4 or mes == 6 or mes == 9 or mes == 11:
        if dia >= 1 and dia <= 30 :
            return True
        else:
            return False
    elif mes == 2 :
        biciesto = es_biciesto(ano)
        if biciesto == True:
            if dia >= 1 and dia <= 29:
                return True
            else:
                return False
        else:
            if dia >= 1 and dia <= 28:
                return True
            else:
                return False
    else:
        return False

def main():
    """
    Contrato:
    Ejecuta el código principal.
    Pre: No recibe nada.
    Post: No retorna nada, solo ejecuta las funciones para validar el dia.
    """

    dia =0
    while dia <= 0 :
       dia = int(input("Ingrese el dia:  "))

    mes = 0 
    while mes <= 0 :
        mes = int(input("Ingrese el mes: "))

    anio = 0 
    while anio <= 0 :
        anio = int(input("Ingrese el año: "))

    if validar_dia(dia, mes, anio) == True:
        print("La fecha es valida.")
    else:
        print ("La fecha es invalida.")


         
main()
         

