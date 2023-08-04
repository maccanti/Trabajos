numero = int(input("Ingresa un número: "))

def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
    
print("El número", numero, "es", es_par_o_impar)
