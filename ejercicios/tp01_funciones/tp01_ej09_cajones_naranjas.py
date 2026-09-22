import random as rn 

def  naranjas(cant_naranjas):
    """
    contrato:
    Calcúla las naranjas y su peso.
    Pre: Recibe un entero positivo que determina la cantidad de naranjas cosechadas.
    post: Retorna tres enteros que determinan la cantidad de cajónes, naranjas y naranjas para jugo.
    """
    n_jugo = 0
    n_cajon = 0
    n_peso = 0

    for i in range(cant_naranjas):
        naranja = rn.randint(150, 350)
        if naranja >= 200 and naranja <= 300:
            n_cajon += 1
            n_peso += naranja

        else:
            n_jugo += 1 
    return n_cajon, n_peso, n_jugo

def camion(peso):
    """
    Contrato:
    Calcula cuántos camiones transportarán las naranjas. 
    Pre: Recibe el peso total de todas las naranjas.
    Post: Retorna un entero positivo que indíca cuantos camiones llevarán las naranjas.
    """
    camiones = 0
    if peso >= 500000:
        camiones = peso // 500000 
        peso %= 500000
    if peso >= 400000:
        camiones += 1
    return camiones 

def cant_cajones(n_cajon):
    cajones = n_cajon// 100
    n_cajon %= 100 

    return cajones, n_cajon


def main():
    """
    Coontrato:
    Ejecuta el código principal
    Pre: No recibe nada.
    Post: No retorna nada, ejecuta todas las funciones.
    """
    cant_naranjas = int(input("Ingrese la cantidad de naranjas cosechadas : "))

    n_cajon, n_peso, n_jugo = naranjas(cant_naranjas)
    cant_cajoness, n_cajon = cant_cajones(n_cajon)
    
    cant_camiones = camion(n_peso)


    print(f"La  cantidad de camiones es de : {cant_camiones}")
    print(f"La cantidad de naranjas para jugo es de : {n_jugo} ")
    print(f"La cantidad de naranjas que sobran es de: {n_cajon}")
    print(f"La cantidad de cajones es de: {cant_cajoness}")


main()




