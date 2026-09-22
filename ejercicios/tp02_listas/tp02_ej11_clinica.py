
def cargar_paciente(pacientes:list[int], condicion: list[int])-> None:
    """
    Carga los pacientes que ingresan a la clínica
      con su tipo de atención. 
    pre: Recibe dos listas:paciente y condicion
    post:Modifica ambas listas agregando números de afiliado de 4 dígitos
    según el tipo de paciente.

    """
    while True:
        afiliado = int(input("Ingrese número de afiliado: "))

        while True:
            if afiliado >= 1000 and afiliado <= 9999:
                break
            elif afiliado == -1:
                break
            else:
                afiliado = int(input("Ingrese otra vez el número de afiliado: "))
            
        if afiliado != -1:
            while True:
                tipo= int(input("Ingrese el tipo de paciente  (0- Urgencia) o (1- Turno): "))
                if tipo == 0 :
                    break
                elif tipo == 1 :
                    break
                else:
                    print("El tipo de paciente es incorrecto ")

            pacientes.append(afiliado)
            condicion.append(tipo)

        else:
            break
        


def mostrar_pacientes(pacientes:list[int] ,condicion:list[int])-> None:
    """
     Muestra los pacientes atendidos según su tipo de atención
        pre: Recibe la lista de pacientes y la lista de condiciones
        post: Muestra primero los pacientes atendidos por urgencia y luego
          los pacientes atendidos por turno en el orden que llegaron .
    """
    print("Pacientes de urgencia: ")
    for i, e in enumerate(pacientes):
        if condicion[i] == 0 :
            print(f"Número de paciente: {e}")
        
    print("Pacientes de Turno: ")
    for i, e in enumerate(pacientes):
        if condicion[i] == 1 :
            print(f"Número de paciente: {e}")


def buscar_afiliado(pacientes:list[int],condicion:list[int])->None:
    """
    Busca un número de afiliado y
     contabiliza si fue atendido por  urgencia y por turno
    pre: Recibe la lista de pacientes y la lista de condiciones
    post:Informa cuántas veces el afiliado  fue atendido por urgencia y cuántas por turno.
    Hasta que se ingresa -1
    """
    while True:
        afiliado = int(input("Ingrese su número de afiliado: "))

        cant_urgencia = 0
        cant_turno = 0 
        if afiliado == -1:
        
            break


        elif afiliado in pacientes :
        
            for i, e in enumerate (pacientes):
                if e == afiliado :
                    if condicion[i] == 0:
                        cant_urgencia += 1

                    elif condicion[i] == 1 :
                        cant_turno += 1

            print(F"La cantidad de veces que ingreso a urgencia es: {cant_urgencia}")
            print(f"La cantidad de veces que ingreso por un turno es: {cant_turno}")

def main()->None:
    """
    Ejecuta el programa principal de atención de pacientes de la clínica. 
    Pre: No recibe parámetros. 
    post:Carga los pacientes y sus tipos de atención, muestra la lista
    de pacientes y permite buscar afiliados para informar la 
    cantidad de cada tipo

    """


    pacientes = []
    condicion=[]

    cargar_paciente(pacientes,condicion)

    mostrar_pacientes(pacientes,condicion)

    buscar_afiliado(pacientes,condicion)

main()


        
        

                


    
        




         
