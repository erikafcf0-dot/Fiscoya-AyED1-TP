def intercalar(lista1 : list[int], lista2: list[int])->None:

    for i, e in enumerate(lista2):
        pos = i*2 + 1
        lista1[pos:pos] = [e]

def main():
    lista1 = [8,1,3]
    lista2 = [5,9,7]

    print("Lista original:")
    print(lista1)

    print("lista 2:")
    print(lista2)

    intercalar(lista1, lista2)

    print("Lista intercalada:")
    print(lista1)

main()

