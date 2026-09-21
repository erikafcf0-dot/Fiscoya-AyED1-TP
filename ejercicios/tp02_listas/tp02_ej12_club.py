def cargar_socios(socios:list[int])-> None:
    """
    Carga los números de socios que ingresan al club .
    pre:Recibe una lista de números enteros.
    post: Modifica la lista agregando los números
      de socios de 5 digitos hasta que el usuario ingrese 0
    """

    while True:

        socio = int(input("Ingrese el número de socio (0 para finalizar): "))

        while True:
            if socio >= 10000 and socio <= 99999:
                break
            
            elif socio == 0 :
                break
            else:
                socio =int(input("Ingrese otra vez el número de socio: ")) 
        if socio != 0:
            socios.append(socio)
        else:
            break


def informar_ingreso(socios: list[int])-> None:
    """
    Informa la cantidad de ingresos de cada socio.
    Pre:Recibe una lista con los números de socios que ingresan.
    Post:Muestra cada socio una sola vez e informa cuántas veces ingresó.
    """
    aux=[]
    for e in socios:
        if e not in aux :
            cantidad = socios.count(e)
            print(f" Socio {e}: ingresó {cantidad} veces:  ")


            aux.append(e)


def eliminar_socio(socios:list[int])-> None:
    """
    Elimina todos los ingresos de un socio .
    pre:Recibe una lista con los números de socios que ingresan.
    post:Modifica la lista eliminando todos los ingresos, muestra los 
    ingresos antes y después de eliminarlos e informa la cantidad 
    de ingresos que se eliminaron.
    """
    socio = int(input("Ingrese el número de socio para dar la baja: "))
    print("Socios actuales")
    print(socios)
    cantidad = socios.count(socio)

    while socio in socios:
        socios.remove(socio)

    print("Socios despues de eliminar ")
    print(socios )
    print(f"La cantidad de ingresos que se eliminaron es : {cantidad}")


def main():
    """
    Ejecuta el programa principal del registro de socios del club.
    pre:No recibe parámetros.
    post: Carga  los ingresos de soccios , informa cuántas veces ingresó
    cada socio y permite eliminar los ingresos.

    """

    socios = []
    cargar_socios(socios)
    print("Informe de ingresos")
    informar_ingreso(socios)
    eliminar_socio(socios)





main()

