


def gasto_subte(cantidad_viajes: int, precio: int)-> int: 
    """
    Contrato: Calcula el precio de todos los viajes incluyendo el descuento.
    pre: Recibe dos enteros positivos que indican la cantidad de viajes y el precio base.
    post: Retorna un flotante que indica el gasto total de todos los viajes.
    """ 
    gasto = 0 
    for i in range(cantidad_viajes):
        if i < 20 :
            gasto += precio

        elif i < 30 :
            gasto += precio * 0.8 

        elif i < 40 :
            gasto += precio * 0.7 

        else :
            gasto += precio * 0.6 


    return gasto 


while True:
        
    cant_viajes = int(input("ingrese cantidad de viajes: "))
    if cant_viajes > 0:
        break
    else:
        print("Error,la cantidad de viajes tiene que ser superior a 0  ")

while True :
    precio =int(input("ingrese precio del viaje : "))
    if precio > 0:
        break
    else:
        print("El precio tiene que ser mayor a 0 ")


gasto_subte(cant_viajes, precio)
