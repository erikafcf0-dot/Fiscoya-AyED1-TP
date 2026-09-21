
def cargar_paciente(pacientes:list[int], condicion: list[int])-> None:
    """
    pre:
    post:

    """

    afiliado = int(input("Ingrese número de afiliado: "))

    while True:
        if afiliado >= 1000 and afiliado <= 9999:
            break
        elif afiliado == -1:

            return afiliado
        else:
            afiliado = int(input("Ingrese otra vez el número de afiliado: "))



         
