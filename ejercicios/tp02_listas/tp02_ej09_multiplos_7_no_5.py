
a =int(input("Ingrese un número: "))
b =int(input("Ingrese otro número: "))

lista = [num for num in range(a,b+1) if num %7 == 0 and num %5 != 0 ]

print(lista)
