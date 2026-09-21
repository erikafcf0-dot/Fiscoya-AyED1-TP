# LIBRERIA
import random as rn

lista = [rn.randint(1,100)for i in range(10) ]

lista1 = list(filter(lambda num:num % 2 !=0, lista))

print("Lista original: ")
print(lista)

print("Lista con impares: ")
print(lista1)