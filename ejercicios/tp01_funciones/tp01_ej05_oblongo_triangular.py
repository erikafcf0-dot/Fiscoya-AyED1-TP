def vericar_oblongo(num):
    """
    


    """
    
    for i in range(num+1):
        if i *(i+1) == num:
            return True
        elif i *(i+1) > num:
            return False 

num = int(input("Ingrese el numero a verificar: " ))

print(vericar_oblongo(num))



def triangular(num):

    num_t= 0
    for i in range(num):
        num_t += i
        if num_t == num :
            return True
        elif num_t > num:
            return False


num = int(input("Ingrese el numero a verificar: " ))

print(triangular(num))

        
