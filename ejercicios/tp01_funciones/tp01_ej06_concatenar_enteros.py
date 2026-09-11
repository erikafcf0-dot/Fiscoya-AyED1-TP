
oracion = "Hola mundo"

no_solucion = [dato.upper() for dato in oracion] (lista por comprension) # cada letra 
print(oracion .split()] # cada palabra 
["hola", "mundo"]




oracion = "hola mundo"
solucion = [dato.upper() for dato in oracion.split()]
print(solucion)



oracion =
solucion =
aux = oracion.split()
for palabra in aux :
    solucion append(palabra.upper())




































































            


















































def concatenar_enteros(num1:int, num2: int) -> int:
    
    """
    contrato:Concatena dos numeros positivos enteros
    pre:recibe dos enteros positivos
    post: un entero positivo formado por ambos parametros recibidos 

    """
    cant_dig = 0
    "aux: int"
    contador = num2 

    while True:
        if contador > 0:
            contador //=  10 
            cant_dig += 1
        else:
            break 
    return num1 * (10 ** cant_dig) + num2

while True:
    num1 = int(input("ingrese un numero: "))
    if num1 <= 0 :
        print("ingrese otro numero")
    else:
        break

while True:
    num2 = int(input("ingrese un numero: "))
    if num2 <= 0 :
        print("ingrese otro numero")
    else:
        break

print(concatenar_enteros(num1, num2))


        






